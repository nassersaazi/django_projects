from . import views
from rest_framework import routers
from django.urls import path,include

router = routers.DefaultRouter()
router.register('users', views.UserView)

urlpatterns = [
    #path('users/', views.UserList.as_view()),
    #path('users/<int:pk>/', views.UserDetail.as_view())
    path('', include(router.urls))
]
