from django.urls import path
from . import views

urlpatterns = [
    path('', views.showDemoPage, name='showDemoPage'),
    path('login/', views.showLoginPage, name='showLoginPage'),
]   
