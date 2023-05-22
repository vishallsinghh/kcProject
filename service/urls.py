from django.contrib import admin
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings



urlpatterns = [
	path('<int:pk>',index.as_view(),name='index'),
	path('<str:slugname>',GetPhoto.as_view(),name="GetPhoto")
]