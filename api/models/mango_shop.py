from django.db import models

class Mango_Shop(models.Model):
    location = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    