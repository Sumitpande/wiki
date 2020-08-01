from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.Entry, name="Entry"),
    path("CreateNewPage/", views.newPage , name="newPage" ),
    path("EditPage/<str:title>", views.editPage , name="editPage" ),
    path("Random/", views.Random, name="Random"),
    path("search/" ,views.search, name="search")
]
