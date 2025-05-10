from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('info/', views.info, name='info'),
    path('menu/', views.menu, name='menu'),
    path('poi/', views.poi, name='poi')
]