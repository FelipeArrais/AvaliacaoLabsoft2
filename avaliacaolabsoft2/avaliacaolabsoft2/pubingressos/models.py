from django.db import models

# Create your models here.
class PubIngresso(models):
    STATUS_CHOICES= [
        (0, 'livre'),
        (1, 'ocupado')
    ]

    fileira = models.CharField(max_lenght=1)
    numero = models.IntegerField()
    status = models.IntegerChoices(choices=STATUS_CHOICES)
