from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='thoughtsnideas-home'),
    path('about/', views.about, name='thoughtsnideas-about'),
]