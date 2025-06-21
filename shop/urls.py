from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('info/', views.info, name='info'),
    path('menu/', views.menu, name='menu'),
    path('poi/', views.poi, name='poi'),
    path('index2/', views.index2, name='index2'),
    path('menu_roads_pay/', views.menu_roads_pay, name='menu_roads_pay'),
    path('RoadPayInfo/AT_road_pay', views.AT_road_pay, name='AT_road_pay'),
    path('RoadPayInfo/DKV_box_setting', views.DKV_box_setting, name='DKV_box_setting'),
    path('RoadPayInfo/HR_road_pay', views.HR_road_pay, name='HR_road_pay'),
    path('RoadPayInfo/CH_road_pay', views.CH_road_pay, name='CH_road_pay'),
    path('RoadPayInfo/GB_road_pay', views.GB_road_pay, name='GB_road_pay'),
    path('link_sites/', views.link_sites, name='link_sites'),
]
