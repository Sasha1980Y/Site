from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('info/', views.info, name='info'),
    path('menu/', views.menu, name='menu'),
    path('poi/', views.poi, name='poi'),
    path('index2/', views.index2, name='index2'),
    path('menu_roads_pay/', views.menu_roads_pay, name='menu_roads_pay'),
    path('RoadPayInfo/', views.AT_road_pay, name='AT_road_pay')
]
