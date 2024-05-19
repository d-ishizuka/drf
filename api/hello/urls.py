from django.urls import path
from .views import HelloView
from . import views

urlpatterns = [
  path('', views.index, name='index'),
]