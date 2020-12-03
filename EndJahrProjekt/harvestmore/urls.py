
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.home,name='admin-home'),
    path('admin/add-user', views.add_user,name='add-user'),
    path('admin/deactivate-user', views.deactivate_user,name='deactivate-user'),
    
]
