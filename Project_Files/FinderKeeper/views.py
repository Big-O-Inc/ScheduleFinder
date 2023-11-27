from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
from .forms import *
from users.models import User 
from django.views.generic import View
from rest_framework.decorators import api_view
from .models import *
import json
import re

day_dict = {'1': "M",
            '2': "T",
            '3': "W",
            '4': "Th",
            '5': "F"}

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
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        # Authenticate user
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)  # Log the user in
            # Redirect to a different page upon successful login
        
            #INSERT WHEREVER USER HAS SCHEDULE
            return redirect('schedule')  # Redirect to the dashboard, change as needed
        else:
            # Invalid login
            return HttpResponse("Invalid login credentials. Please try again.")
        
class Logout(View):
    def get(self, request):
        pass 
    
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return redirect('homepage')

'''
Creating account info for user (username and password), secure their info, and associate their account to a uuid
'''
class Signup(View):
    def get(self, request):
        return render(request, 'FinderKeeper/signup.html')
    def post(self, request):
        # Assuming the form fields are 'email', 'username', and 'password'
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Create a new user
        try:
            user = User.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
        except:
            return HttpResponse("Account already exists")
        
        # Redirect to the login page after successful sign-up
        return redirect('login')
'''
Creates and populates a schedule with events of the user (searched by uuid). 
Can add, update, and delete events associated with uid.
'''
class Scheduler(View):
    #Creates the scheduler and populates it with events from the user
    def get(self, request):
        form = AddEventForm()
        if request.user.is_authenticated:
            user_sched = Event.objects.filter(uid=request.user).values() 
            context = {
                'eventData':user_sched,
                'eventJson':json.dumps(list(user_sched), cls=DjangoJSONEncoder),
                'form':form,
            }
            return render(request, 'FinderKeeper/schedule.html', context,)
        else:  #If user is not logged in, just direct them to an empty schedule 
            return render(request, 'FinderKeeper/schedule.html',{'form':form})
        
    #Handles changes to users schedule
    def post(self, request):
        if request.user.is_authenticated:
            method = self.request.POST.get('_method', '').lower()
            if method == 'add':
                self.add(request)
            elif method == 'edit':
                self.edit(request)
            elif method == 'delete':
                self.delete(request)
        else:
            return HttpResponse("Must login first")
        return redirect('schedule')

    #Adding classes/event
    def add(self, request):
        form = AddEventForm(request.POST)
        if form.is_valid(): 
            Event.objects.create(uid=request.user,
                                 title=form.cleaned_data.get("title"),
                                 day=form.cleaned_data.get("days"),
                                 startTime=form.cleaned_data.get("startTime"),
                                 endTime=form.cleaned_data.get("endTime"),
                                 location=form.cleaned_data.get("location"),
                                 mapData=self.findBldg(form.cleaned_data.get("location")), #If location is valid will return a link, otherwise None
                                 description=form.cleaned_data.get("description")) 

    #Update classes/events
    def edit(self, request):
        eventId = request.POST.get('editList')
        userEvent = Event.objects.filter(uid=request.user)
        editEvent = userEvent.get(id=eventId)

        editEvent.title = request.POST.get("title")
        editEvent.day = request.POST.getlist("dayList")
        editEvent.startTime = request.POST.get("startTime")
        editEvent.endTime = request.POST.get("endTime")
        editEvent.location = request.POST.get("location")
        editEvent.description = request.POST.get("description")
        editEvent.mapData = self.findBldg(editEvent.location)
        editEvent.save()
        
    #Delete classes/event
    def delete(self, request):
        form = request.POST.getlist('delList')
        if len(form) != 0:
            userEvents = Event.objects.filter(uid=request.user)
            for id in form:
                userEvents.filter(id=id).delete()

    def findBldg(self, str):
        parsed = re.split("\W+", str)
        for x in parsed:
            if len(x) > 0 and bool(re.search(r'\d',x)): #Searches for first valid instance of a string matching a valid building number format
                if Building.objects.filter(bldg=x.upper()).exists(): #Assumes building number is given first. If this is not valid then assume rest of string does not contain building number
                    bldg = Building.objects.filter(bldg=x.upper())
                    mapData = bldg.values_list('link', flat=True)
                    return mapData[0]
                else:
                    return None
        return None
                
'''
Produces a map of the campus, allows users to pin/highlight buildings for easier navigation
Interacts with the Scheduler class to autmoatically pin the buildings of the user's classes 
'''
class CampusMap(View):
    def get(self, request):
        return render(request, 'FinderKeeper/map.html')

'''
Has settings for web application that gives the user option to
- Log out of their account
-
'''
class Settings(View):
    def get(self, request):
        return render(request, 'FinderKeeper/settings.html')