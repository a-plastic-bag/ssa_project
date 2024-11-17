from django.urls import path
from two_factor.urls import urlpatterns as tf_urls
from . import views

urlpatterns = [
    path("", views.user, name="user"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register/", views.register, name="register"),
    path("mfa/", include(tf_urls)),  # Add the two-factor authentication URLs
]
