from django.urls import path

from . import views

urlpatterns = [
    path("", views.index),
    path("map", views.get_map),
    path("buildings", views.building_cord)
]
