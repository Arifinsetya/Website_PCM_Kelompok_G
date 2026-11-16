from django.contrib import admin
from .models import Pengurus

@admin.register(Pengurus)
class PengurusAdmin(admin.ModelAdmin):
    list_display = ('nama', 'jabatan', 'bidang', 'urutan')
    search_fields = ('nama', 'jabatan')