from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>", views.title, name="title"),
    path("title/new", views.createNewTitle, name="createNewTitle"),
    path("title/<int:title_id>/new-entry", views.createEntry, name="createEntry"),
    path("title/<int:title_id>/<int:entry_id>/like", views.like, name="like"),
    path("title/<int:title_id>/<int:entry_id>/dislike", views.dislike, name="dislike"),
    path("title/create", views.saveTitle, name="saveTitle")
] 