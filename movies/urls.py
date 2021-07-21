from django.urls import path

from . import views

urlpatterns = [
    path('hello', views.hello, name='hello'),
    path('import', views.import_csv),
    path('show', views.dump_csv),
]
