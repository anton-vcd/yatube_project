# posts/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    # posts web
    path('group', views.group_posts),
    path('group/<int:pk>/', views.group_posts_detail),
    path('group/<slug:pk>/', views.group_posts_slug),
] 