from django.urls import path
from . import views

urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name = "logout"),
    path("user/<str:username>/", views.user_details, name = "user_details"),
    path("user/<str:username>/edit", views.edit_user, name = "edit_user"),
    path("user/<str:username>/edit/done", views.change_user, name = "change_user"),
]