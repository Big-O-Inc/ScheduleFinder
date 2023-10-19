from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Days(models.IntegerChoices):
    Monday = 1, "Monday"
    Tuesday = 2, "Tuesday"
    Wednesday = 3, "Wednesday"
    Thursday = 4, "Thursday"
    Firday = 5, "Friday"

class Event(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    day = models.IntegerField(choices=Days.choices, default=Days.Monday)
    startTime = models.TimeField(null=True)
    endTime = models.TimeField(null=True)
    location = models.CharField(max_length=200)
    description = models.TextField()