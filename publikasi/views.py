from django.shortcuts import render, get_object_or_404
from .models import Artikel

def daftar(request):
    artikel = Artikel.objects.filter(terbit=True)
    return render(request, 'publikasi/daftar.html', {'artikel': artikel})

def detail(request, slug):
    artikel = get_object_or_404(Artikel, slug=slug, terbit=True)
    return render(request, 'publikasi/detail.html', {'a': artikel})