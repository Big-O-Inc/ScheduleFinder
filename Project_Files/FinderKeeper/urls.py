from django.urls import path
import uuid
from . import views

urlpatterns = [
    path("", views.Homepage.as_view(), name='homepage'),
    path("map", views.CampusMap.as_view(), name='map'),
    path("schedule", views.Scheduler.as_view(), name='schedule'),
    path("schedule/<uuid:userId>", views.Scheduler.as_view(), name='schedule'),
    path("login", views.Login.as_view(), name='login'),
    path("signup", views.Signup.as_view(), name='signup')
]

