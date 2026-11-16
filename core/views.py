from django.shortcuts import render
from publikasi.models import Artikel
from organisasi.models import Pengurus

def beranda(request):
    return render(request, 'core/beranda.html', {
        'artikel_terbaru': Artikel.objects.filter(terbit=True)[:3],
        'pengurus': Pengurus.objects.all()[:4],
    })

def tentang(request):
    return render(request, 'core/tentang.html')