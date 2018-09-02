from django.db import models

class Product(models.Model):
    image = models.ImageField(upload_to='images/')
    summary = models.CharField(max_length=200)
