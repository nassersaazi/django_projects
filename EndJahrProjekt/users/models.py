from django.db import models
from django.contrib.auth.models import User
from harvestmore.models import UserRole
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    area = models.CharField(max_length=30, blank=True)
    phone = models.CharField(null=True,max_length=30, blank=True)
    role = models.ForeignKey(UserRole, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.username