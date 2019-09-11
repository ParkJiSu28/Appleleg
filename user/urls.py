from django.urls import path, include
from .views import UserViewSet
from rest_framework.routers import DefaultRouter


routers = DefaultRouter()
routers.register('', UserViewSet)

urlpatterns = [
    path('', include(routers.urls)),
]
