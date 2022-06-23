# from turtle import color
from django.db import models

class Mango(models.Model):
    color = models.CharField(max_length=100)
    ripe = models.BooleanField(default=False)
    mango_shop = models.ForeignKey('Mango_Shop', related_name='mangos', on_delete=models.CASCADE, null=True)
