from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PesanForm

def form(request):
    if request.method == 'POST':
        f = PesanForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Pesan berhasil dikirim. Terima kasih!')
            return redirect('kontak:form')
    else:
        f = PesanForm()
    return render(request, 'kontak/form.html', {'form': f})