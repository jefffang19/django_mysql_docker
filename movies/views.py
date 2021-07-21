from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from movies.models import Movie


def hello(request):
    return HttpResponse("Hello, world.")


def import_csv(request):
    import pandas as pd

    df = pd.read_csv('ratings_small.csv')

    for i in range(100):
        # Model
        m = Movie(user_id=int(df.iloc[i]['userId']), movie_id=int(df.iloc[i]
                                                                  ['movieId']), rating=float(df.iloc[i]['rating']))
        m.save()

    return HttpResponse('Import csv complete')


def dump_csv(request):
    m = Movie.objects.all()
    return HttpResponse([i.user_id for i in m])
