import pandas


def insert_or_update_records(df, db_connection):
    """

    :param df: dataframe with the following schema:
        segment id[int],
        rank[int],
        total_entries[int],
        num_attempts[int],
        read_date[datetime]
    :type df: pandas.DataFrame
    :param db_connection: connection to postgresql database
    :type db_connection: psycopg2 connection
    :return: None
    """

    cursor = db_connection.cursor()

    cursor.execute('SELECT * FROM my_leaderboard;')

    primary_key_set = set([record[0] for record in cursor.fetchall()])

    df['update'] = df['segment_id'].apply(lambda x: x in primary_key_set)

    update_df = df[df['update'] == True]
    update_records(update_df, db_connection)

    df = df[df['update'] == False]
    insert_records(df, db_connection)

    return


def insert_records(df, db_connection):

    cursor = db_connection.cursor()

    insert_into_command_str = 'INSERT INTO my_leaderboard (segment_id, rank, total_entries, num_attempts, read_date) VALUES '
    for record in df.to_dict('records'):
        insert_into_command_str += \
            '(' + \
            str(record['segment_id']) + ', ' + \
            str(record['viewer_rank']) + ', ' + \
            str(record['total_entries']) + ', ' + \
            str(record['frequency']) + ', \'' + \
            str(record['read_date']) + '\'' + \
            '),'
    insert_into_command_str = insert_into_command_str[:-1] + ';'

    cursor.execute(insert_into_command_str)

    db_connection.commit()

    return


def update_records(df, db_connection):

    cursor = db_connection.cursor()

    for record in df.to_dict('records'):
        insert_into_command_str = 'UPDATE my_leaderboard SET '
        insert_into_command_str += \
            'rank = ' + str(record['viewer_rank']) + ', ' + \
            'total_entries = ' + str(record['total_entries']) + ', ' + \
            'num_attempts = ' + str(record['frequency']) + ', ' + \
            'read_date = \'' + str(record['read_date']) + '\'' + \
            ' WHERE segment_id = ' + str(record['segment_id']) + ';'

        cursor.execute(insert_into_command_str)

    db_connection.commit()

    return
