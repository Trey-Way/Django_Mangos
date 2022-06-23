from api.serializers.mango_shop import Mango_ShopSerializer
from rest_framework import serializers
from ..models.mango import Mango
class MangoWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Mango
        fields = ('id', 'color', 'ripe', 'mango_shop')