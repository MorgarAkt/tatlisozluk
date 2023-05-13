from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>", views.title, name="title"),
    path("title/search", views.search, name="search"),
    path("title/new", views.createNewTitle, name="createNewTitle"),
    path("title/<int:title_id>/new-entry", views.createEntry, name="createEntry"),
    path("entry/<int:entry_id>/delete", views.deleteEntry, name="deleteEntry"),
    path("entry/<int:entry_id>/edit", views.editEntry, name="editEntry"),
    path("title/<int:title_id>/entry/<int:entry_id>/edit", views.changeEntry, name="changeEntry"),
    path("title/<int:title_id>/<int:entry_id>/like", views.like, name="like"),
    path("title/<int:title_id>/<int:entry_id>/dislike", views.dislike, name="dislike"),
    path("title/create", views.saveTitle, name="saveTitle")
] 