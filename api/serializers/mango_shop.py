from unicodedata import name
from rest_framework import serializers
from ..models.mango_shop import Mango_Shop

class Mango_ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mango_Shop
        fields = ('id', 'location', 'name')
