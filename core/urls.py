from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # homepage
    path('design/', views.design, name='design'),
]