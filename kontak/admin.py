from django.contrib import admin
from .models import Pesan

@admin.register(Pesan)
class PesanAdmin(admin.ModelAdmin):
    list_display = ('nama', 'email', 'subjek', 'tanggal', 'dibaca')
    list_filter = ('dibaca',)