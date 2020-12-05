
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home,name='admin-home'),
    # path('login', views.login,name='login'),
    # path('register', views.register,name='register'),
    # path('add-user', views.add_user,name='add-user'),
    # path('deactivate-user', views.deactivate_user,name='deactivate-user'),
    
]
