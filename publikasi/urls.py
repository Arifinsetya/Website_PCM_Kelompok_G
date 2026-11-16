from django.urls import path
from . import views

app_name = 'publikasi'
urlpatterns = [
    path('', views.daftar, name='daftar'),
    path('<slug:slug>/', views.detail, name='detail'),
]