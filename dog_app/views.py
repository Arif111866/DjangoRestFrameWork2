from django.shortcuts import render
from rest_framework.views import APIView
from .models import Bread
from .serializer import Breadserializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
# Create your views here.


class BreadList(APIView):
    def get(self, request):
        breads = Bread.objects.all()
        serializer = Breadserializer(breads,  many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Breadserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BreadDetail(APIView):
    def get_object(self, pk):
        try:
            return Bread.objects.get(pk=pk)
        except Bread.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        bread = self.get_object(pk)
        serializer = Breadserializer(bread)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        bread = self.get_object(pk)
        serializer = Breadserializer(bread, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Bread = self.get_object(pk)
        Bread.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
