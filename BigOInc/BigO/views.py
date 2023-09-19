from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view

def index(request):
    return render(request, 'index.html')

#Benjamin: An http get method that will respond with a map image from the map.html file
def get_map(request):
    if request.method == 'GET':
        return render(request, 'map.html')