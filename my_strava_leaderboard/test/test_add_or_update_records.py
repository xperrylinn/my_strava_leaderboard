import os
import pandas
import psycopg2
from my_strava_leaderboard.insert_or_update_records import (
    insert_or_update_records,
    insert_records,
    update_records
)


connection = psycopg2.connect(
    dbname='my_strava_leaderboard',
    user=os.environ['POSTGRES_USERNAME'],
    password=os.environ['POSTGRES_PASSWORD']
)

cursor = connection.cursor()


def test_insert_records():

    initial_db_snapshot = pandas.read_csv('./test_data/my_strava_leaderboard_test_data_initial.csv')

    insert_records(initial_db_snapshot, connection)

    assert True


def test_update_records():

    new_data = pandas.read_csv('./test_data/my_strava_leaderboard_test_data_new_data.csv')

    update_records(new_data, connection)

    assert True


def test_insert_or_update_records():

    new_data = pandas.read_csv('./test_data/my_strava_leaderboard_test_data_new_data.csv')
    final_db_snapshot = pandas.read_csv('./test_data/my_strava_leaderboard_test_data_final.csv')

    insert_or_update_records(new_data, connection)

    assert True


test_insert_or_update_records()
# test_insert_records()
# test_update_records()

connection.close()
