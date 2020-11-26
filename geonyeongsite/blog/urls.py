from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('enroll/',views.enroll, name='enroll'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
    path('<int:blog_id>/edit', views.edit, name='edit'),
]