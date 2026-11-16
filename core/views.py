from django.shortcuts import render

def beranda(request):
    return render(request, 'core/beranda.html')

def tentang(request):
    return render(request, 'core/tentang.html')