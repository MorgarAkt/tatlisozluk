from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("<str:slug>", views.title, name="title"),
    path("title/<int:title_id>/<int:entry_id>/like", views.like, name="like"),
    path("title/<int:title_id>/<int:entry_id>/dislike", views.dislike, name="dislike"),
]