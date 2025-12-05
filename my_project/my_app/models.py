from django.db import models

class student(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=20, blank=True, null=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)    