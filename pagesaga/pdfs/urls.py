from django.urls import path
from .views import getBooks, home


urlpatterns=[
    path("", home, name="home"),
    path("api/books/", getBooks, name="getbooks")
]
