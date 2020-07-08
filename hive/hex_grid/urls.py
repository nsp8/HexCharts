from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='hex-home'),
    path('about/', views.about, name='hex-about'),
]
