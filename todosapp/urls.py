from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='todos-index'),
    path('base/', views.base, name='todos-base'),
]