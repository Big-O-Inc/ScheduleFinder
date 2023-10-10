from django.db import models
from django.utils import timezone
import uuid

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class Event(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    startDate = models.DateTimeField(default=timezone.now())
    endDate = models.DateTimeField(default=timezone.now())
    location = models.CharField(max_length=200)
    description = models.TextField()