from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.mango import Mango
from ..serializers.mango import MangoSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..serializers.mango_write import MangoWriteSerializer

class MangosView(APIView):
    def post(self, request):
        mango = MangoWriteSerializer(data=request.data)
        if mango.is_valid():
            mango.save()
            return Response(mango.data, status=status.HTTP_201_CREATED)
        else:
            return Response(mango.errors, status=status.HTTP_400_BAD_REQUEST)  

    def get(self, request):
        mangos = Mango.objects.all()
        data = MangoSerializer(mangos, many=True).data
        return Response(data)

class MangoView(APIView):
    def delete(self, request, pk):
        mango = get_object_or_404(Mango, pk=pk)
        mango.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk):
        mango = get_object_or_404(Mango, pk=pk)
        updated_mango = MangoSerializer(mango, data=request.data)
        if updated_mango.is_valid():
            updated_mango.save()
            return Response(updated_mango.data)
        else:
            return Response(updated_mango.errors, status=status.HTTP_400_BAD_REQUEST)
