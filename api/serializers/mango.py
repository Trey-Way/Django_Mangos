from api.serializers.mango_shop import Mango_ShopSerializer
from rest_framework import serializers
from ..models.mango import Mango
from ..serializers.mango_shop import Mango_ShopSerializer

class MangoSerializer(serializers.ModelSerializer):
    mango_shop = Mango_ShopSerializer(many=False)

    class Meta:
        model = Mango
        fields = ('id', 'color', 'ripe', 'mango_shop')
