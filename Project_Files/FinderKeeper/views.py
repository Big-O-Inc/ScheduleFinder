from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
import pandas as pd
from geopy.geocoders import Nominatim
from .models import *

def index(request):
    return render(request, 'index.html')

#Benjamin (for A3): An http get method that will respond with a map image from the map.html file
@api_view(['GET'])
def get_map(request):
    return render(request, 'map.html')
    
#Joshua: An http get method that will retrieve the settings menu
def get_settings(request):
    if request.method == "GET":
        return render(request, 'settings.html')
    
#Benjamin (for A4): Using the pandas library to read and display data from json formatted data. Found at endpoint /buildings
@api_view(['GET'])
def building_cord(request):
    #For now, will have the data of a few buildings stored in a variable. Will move all of this to a database later
    #Keys are the building numbers, and the value is a dictionary holding the college of the building and the latitude and longitude coordinates.
    data = {'5': {'Building':'College of Letters, Arts, and Social Sciences', 'Latitude':34.057845973368906, 'Longitude':-117.82442360649715},
            '7': {'Building':'College of Environmental Design', 'Latitude':34.05773931072947, 'Longitude':-117.8274276805938},
            '8': {'Building':'College of Science', 'Latitude':34.05891259222622, 'Longitude':-117.82488494644772}, 
            '9': {'Building':'College of Engineering', 'Latitude':34.05925924046298, 'Longitude':-117.82234221230162},
            '17':{'Building':'College of Engineering', 'Latitude':34.06006808083938, 'Longitude':-117.82120495567929},
            '163':{'Building':'College of Business Administration','Latitude':34.06137465285341, 'Longitude':-117.82046466599118}}
    df = pd.DataFrame(data)
    #Displays a very basic table of the data (in the final product this table will be unnecessary)
    return HttpResponse(df.to_html())

#Joshua Bicera (for A4): Using geopy to return the user's current location (WIP)
@api_view(['GET'])
def get_user_location(request):
    #Simulate the user's location (replace with actual geolocation logic)
    #Will need to have a map layout to return specific cordinates
    user_address = "3801 W Temple Ave, Pomona, CA 91768" #Simulated user address

    geolocator = Nominatim(user_agent="my_geocoder") #Initialize the geocoder
    user_coordinates = {}

    #Geocode the user's address to get coordinates
    location = geolocator.geocode(user_address)
    if location:
        user_coordinates['User'] = {
            'Latitude': location.latitude,
            'Longitude': location.longitude,
        }

    return user_coordinates

@api_view(['GET'])
def load_sched(request):
    #Pulls the specific events that belongs to this user
    #user_sched = Event.objects.filter(uid=userID).values() #Need to figure out how to get the userID
    #For now just pull every data 
    schedule = Event.objects.all().values()
    return render(request
                  , 'FinderKeeper/schedule.html' #HTML to create calendar
                  , {
                      'schedData':schedule, #Data to populate the calendar
                    },)

@api_view(['POST'])
def add_event(request, user_id):
    try:
        Event.objects.create(uid=user_id, title=request.POST["title"], startDate=request.POST["startDate"]
                            , endDate=request.POST["endDate"], location=request.POST["location"]
                            , description=request.POST["description"])
    except(...):
        #Need to figure what could cause errors and how to handle each of them, do nothing for now
        pass