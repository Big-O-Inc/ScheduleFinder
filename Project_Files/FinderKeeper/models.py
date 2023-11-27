from django.db import models
from django.conf import settings
from django.utils import timezone
from multiselectfield import MultiSelectField

day_choices = ((1, "Monday"),
               (2, "Tuesday"),
               (3, "Wednesday"),
               (4, "Thursday"),
               (5, "Friday"))

#Note, using Django auto created 'id' field as primary key 
class Event(models.Model):
    uid = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    day = MultiSelectField(choices=day_choices, max_length=5)
    startTime = models.TimeField()
    endTime = models.TimeField()
    location = models.CharField(max_length=200)
    mapData = models.URLField(null=True)
    description = models.TextField(null=True)

class Building(models.Model):
    bldg = models.CharField(max_length=50) #The building number such as 8 or 24C
    link = models.URLField()
