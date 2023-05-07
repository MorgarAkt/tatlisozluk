from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("title/<int:title_id>", views.title, name="title"),
    path("title/<int:title_id>/<int:entry_id>/<str:like_or_dislike>", views.like_or_dislike, name="like_or_dislike"),
]