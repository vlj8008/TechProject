
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include
from django.contrib import admin
from django.urls import path
from .import views

# URL patterns define what type of additional info is being passed
urlpatterns = [
    path('admin_console', views.admin_console, name="admin_console"),
    path('<int:pk>/details/', views.details, name="details"),
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/confirmDelete/', views.confirmed, name="confirmed"),
    path('createRecord', views.createRecord, name="createRecord"),
]