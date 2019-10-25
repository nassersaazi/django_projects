from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Songs

# Register your models here.
admin.site.site_header = 'Music Service Admin Page'
admin.site.register(Songs)
admin.site.unregister(Group)
