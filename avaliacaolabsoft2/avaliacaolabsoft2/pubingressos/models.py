from django.db import models

# Create your models here.
STATUS_CHOICES= [
    (0, 'livre'),
    (1, 'ocupado')
]

class PubIngresso(models.Model):
    fileira = models.CharField(max_length=1)
    numero = models.IntegerField()
    status = models.IntegerField(choices=STATUS_CHOICES)
