from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name='detail'),
    path('enroll/',views.enroll, name='enroll'),
    path('create/',views.create, name='create'),
    path('<int:blog_id>/delete', views.delete, name='delete'),
]