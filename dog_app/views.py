from django.shortcuts import render
from rest_framework.views import APIView
from .models import Bread,Dog
from .serializer import Breadserializer
from .serializer import Dogserializer
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


class DogList(APIView):
    def get(self, request):
        dogs = Dog.objects.all()
        serializer = Dogserializer(dogs,  many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Dogserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    def get_object(self, pk):
        try:
            return Dog.objects.get(pk=pk)
        except Dog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        dogs = self.get_object(pk)
        serializer = Dogserializer(dogs)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        dogs = self.get_object(pk)
        serializer = Dogserializer(dogs, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        dogs = self.get_object(pk)
        dogs.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)