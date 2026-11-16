from django.contrib import admin
from .models import Kategori, Artikel

admin.site.register(Kategori)

@admin.register(Artikel)
class ArtikelAdmin(admin.ModelAdmin):
    list_display = ('judul', 'kategori', 'tanggal', 'terbit')
    list_filter = ('kategori', 'terbit')
    search_fields = ('judul', 'isi')
    prepopulated_fields = {'slug': ('judul',)}