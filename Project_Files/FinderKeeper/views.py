from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import View
from rest_framework.decorators import api_view
import pandas as pd
from geopy.geocoders import Nominatim
from .models import *

'''
Loads the home page of the website 
'''
class Homepage(View):
    def get(self, request):
        return render(request, 'FinderKeeper/index.html')

'''
Asks for username and password and will fetch the uuid from database if user has an account
'''
class Login(View):
    def get(self, request):
        return render(request, 'FinderKeeper/login.html')
    
'''
Creating account info for user (username and password), secure their info, and associate their account to a uuid
'''
class Signup(View):
    def get(self, request):
        return render(request, 'FinderKeeper/signup.html')

'''
Creates and populates a schedule with events of the user (searched by uuid). 
Can add, update, and delete events associated with uid.
'''
class Scheduler(View):
    def get(self, request, userId='None'): #Creates the scheduler and populates it with events from the user
        if (userId == 'None'):
            return render(request, 'FinderKeeper/schedule.html')
        
        user_sched = Event.objects.filter(uid=userId).values() #Need to figure out how to get the userID
        context = {
            'eventData':user_sched,
        }
        return render(request, 'FinderKeeper/schedule.html', context,)

    def put(self, request, userId): #Adding classes/event
        try:
            Event.objects.create(uid=userId, title=request.POST["title"], startDate=request.POST["startDate"]
                            , endDate=request.POST["endDate"], location=request.POST["location"]
                            , description=request.POST["description"])
        except(...):
            #Need to figure what could cause errors and how to handle each of them, do nothing for now
            pass

    def post(self, request): #Update classes/event
        pass

    def delete(self, request): #Delete classes/event
        pass

'''
Produces a map of the campus, allows users to pin/highlight buildings for easier navigation
Interacts with the Scheduler class to autmoatically pin the buildings of the user's classes 
'''
class CampusMap(View):
    def get(self, request):
        return render(request, 'FinderKeeper/map.html')