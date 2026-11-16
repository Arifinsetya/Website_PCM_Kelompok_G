from django.shortcuts import render
from .models import Pengurus

def daftar(request):
    return render(request, 'organisasi/daftar.html', {'pengurus': Pengurus.objects.all()})