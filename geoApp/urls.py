from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
   path('',views.home, name='home'),
   path('download/shapefile/<str:filename>/', views.download_shapefile, name='download_shapefile'),
   path('download/csv/<str:filename>/', views.download_csv, name='download_csv'),
]