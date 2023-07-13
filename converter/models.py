from django.db import models

class QRCode(models.Model):
    code = models.ImageField(upload_to='qr_codes/')
    data = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'QR Code: {self.pk}'



# Create your models here.
