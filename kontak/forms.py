from django import forms
from .models import Pesan

class PesanForm(forms.ModelForm):
    class Meta:
        model = Pesan
        fields = ['nama', 'email', 'subjek', 'isi']