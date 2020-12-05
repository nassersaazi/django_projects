from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class UserRole(models.Model):
    roleNumber = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Image(models.Model):
    path = models.ImageField(default='default.jpg',upload_to='cassava_images')
    uploader = models.ForeignKey(User, on_delete=models.CASCADE)
    date_uploaded = models.DateTimeField(default=timezone.now)
    labelled = models.BooleanField()

    def __str__(self):
        return self.path

class Notification(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    description = models.TextField()
    event_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



