from django.db import models

# Create your models here.

from django.db import models

class CurrencyRate(models.Model):
    source_currency = models.CharField(max_length=3)
    target_currency = models.CharField(max_length=3)
    exchange_rate = models.DecimalField(max_digits=10, decimal_places=4)
