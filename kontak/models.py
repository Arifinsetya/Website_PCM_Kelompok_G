from django.db import models

class Pesan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    subjek = models.CharField(max_length=150)
    isi = models.TextField()
    tanggal = models.DateTimeField(auto_now_add=True)
    dibaca = models.BooleanField(default=False)

    class Meta:
        ordering = ['-tanggal']
        verbose_name_plural = 'Pesan'

    def __str__(self):
        return f'{self.nama}: {self.subjek}'