from django.db import models
from django.utils.text import slugify

class Kategori(models.Model):
    nama = models.CharField(max_length=60, unique=True)

    class Meta:
        verbose_name_plural = 'Kategori'

    def __str__(self):
        return self.nama

class Artikel(models.Model):
    judul = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    gambar = models.ImageField(upload_to='artikel/', blank=True, null=True)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    terbit = models.BooleanField(default=True)

    class Meta:
        ordering = ['-tanggal']
        verbose_name_plural = 'Artikel'

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.judul)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.judul