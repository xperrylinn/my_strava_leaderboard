from django.http import HttpResponse
from sqlalchemy import create_engine
import pandas
import os


def index(request):

    connection_string = 'postgresql://' + \
                        os.environ['POSTGRES_USERNAME'] + ':' + \
                        os.environ['POSTGRES_PASSWORD'] + '@' + \
                        'localhost:5432/my_strava_leaderboard'

    engine = create_engine(connection_string)

    df = pandas.read_sql_query(
        'SELECT * FROM my_leaderboard;',
        engine
    )

    return HttpResponse(df.to_string())
