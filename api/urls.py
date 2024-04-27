# from django.urls import path, include
# from api import views

# urlpatterns = [
#     path('', views.index, name="index"),
# ]

#Esta es la forma de crear las rutas para aplicacion
#Una api rest con django rest_framework

from rest_framework import routers
from .api import ApiViewSet


ruta = routers.DefaultRouter()
ruta.register('api/employee', ApiViewSet, 'api')

urlpatterns = ruta.urls


