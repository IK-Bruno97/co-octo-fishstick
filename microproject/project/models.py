from django.db import models

# Create your models here.
class MultiForm(models.Model):
    store_name = models.CharField(max_length=50, null=True, blank=True)
    balance = models.DecimalField(default=0, null=True, blank=True, decimal_places=2, max_digits=10)
    price = models.DecimalField(default=0, null=True, blank=True, decimal_places=2, max_digits=10)
    network = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    email = models.CharField(max_length=250, null=True, blank=True)
