from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.mango_shop import Mango_Shop
from ..serializers.mango_shop import Mango_ShopSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404

class Mango_ShopsView(APIView):
    def get(self, request):
        mango_shop = Mango_Shop.objects.all()
        data = Mango_ShopSerializer(mango_shop, many=True).data
        return Response(data)
    
    def post(self, request):
        mango_shop = Mango_ShopSerializer(data=request.data)
        if mango_shop.is_valid():
            mango_shop.save()
            return Response(mango_shop.data, status=status.HTTP_201_CREATED)
        else:
            return Response(mango_shop.errors, status=status.HTTP_400_BAD_REQUEST)
            
class Mango_ShopView(APIView):
    def delete(self, request, pk):
        mango_shop = get_object_or_404(Mango_Shop, pk=pk)
        mango_shop.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, pk):
        mango_shop = get_object_or_404(Mango_Shop, pk=pk)
        updated_shop = Mango_ShopSerializer(mango_shop, data=request.data)
        if updated_shop.is_valid():
            updated_shop.save()
            return Response(updated_shop.data)
        else:
            return Response(updated_shop.errors, status=status.HTTP_400_BAD_REQUEST)
