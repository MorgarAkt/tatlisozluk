from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("title/<int:title_id>", views.title, name="title"),
]