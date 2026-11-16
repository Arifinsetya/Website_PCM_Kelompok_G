from django.urls import path
from . import views

app_name = 'organisasi'
urlpatterns = [path('', views.daftar, name='daftar')]