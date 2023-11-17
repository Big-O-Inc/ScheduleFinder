from django.urls import path
import uuid
from . import views, custom_logout

urlpatterns = [
    path("", views.Homepage.as_view(), name='homepage'),
    path("map", views.CampusMap.as_view(), name='map'),
    path("schedule", views.Scheduler.as_view(), name='schedule'),
    path("login", views.Login.as_view(), name='login'),
     path('settings/', views.Settings.as_view(), name='settings'),
    path('logout/', custom_logout, name='logout'),
    path("signup", views.Signup.as_view(), name='signup')
]

