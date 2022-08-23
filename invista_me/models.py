from datetime import datetime
from django.db import models

# Create your models here.
class Investimento(models.Model):
    investimento = models.TextField(max_length=255)
    valor = models.FloatField()
    pago = models.BooleanField(default=False)
    data = models.DateField(datetime.now)
    