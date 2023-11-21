from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.Homepage.as_view(), name='homepage'),
    path("map", views.CampusMap.as_view(), name='map'),
    path("schedule", views.Scheduler.as_view(), name='schedule'),
    path("login", views.Login.as_view(), name='login'),
    path('settings/', views.Settings.as_view(), name='settings'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path("signup", views.Signup.as_view(), name='signup'),
]

