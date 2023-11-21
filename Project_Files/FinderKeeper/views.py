from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
#from django.contrib.auth.models import User
from .forms import *
from users.models import User 
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
        if request.user.is_authenticated:
            print(request.user.id)
            
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
        user = User.objects.create_user(username=username, email=email)
        user.set_password(password)
        user.save()
        
        # Redirect to the login page after successful sign-up
        return redirect('FinderKeeper/login')
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
            
            for x in user_sched:
                print(x['id'])

            context = {
                'eventData':user_sched,
                'form':form,
            }
            return render(request, 'FinderKeeper/schedule.html', context,)
        else:  #If user is not logged in, just direct them to an empty schedule 
            print("Not logged in")
            return render(request, 'FinderKeeper/schedule.html',{'form':form})
        
    #Handles changes to users schedule
    def post(self, request):
        if request.user.is_authenticated:
            method = self.request.POST.get('_method', '').lower()
            if method == 'add':
                self.add(request)
            elif method == 'update':
                self.update(request) 
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
                                 description=form.cleaned_data.get("description")) 

    #Update classes/event
    def update(self, request):
        pass

    #Delete classes/event
    def delete(self, request):
        pass

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