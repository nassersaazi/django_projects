from django.contrib import admin
from .models import Notification,Event,UserRole,Image

# Register your models here.

admin.site.register(Notification)
admin.site.register(Event)
admin.site.register(UserRole)
admin.site.register(Image)