from django.views.generic.base import TemplateView
from django.http import HttpResponse
from sqlalchemy import create_engine
from my_leaderboard.models import MyLeaderboard
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


class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['records'] = MyLeaderboard.objects.all()
        return context
