from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView, status, Response
from . import models
from . import serializers


# user api
class GetUsers(APIView):
    def get(self, request):
        query = models.User.objects.all()
        serializer = serializers.UserSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateUser(APIView):
    def put(self, request, pk):
        query = models.User.objects.get(pk=pk)
        serializer = serializers.UserSerializers(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostUser(APIView):
    def post(self, request):
        serializer = serializers.UserSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchUser(APIView):
    def get(self, request):
        search = request.GET['name']
        query = models.User.objects.filter(question_text__contains=search)
        serializer = serializers.UserSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteUser(APIView):
    def delete(self, request, pk):
        query = models.User.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# spot api
class GetSpot(APIView):
    def get(self, request):
        query = models.Spot.objects.all()
        serializer = serializers.SpotSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UpdateSpot(APIView):
    def put(self, request, pk):
        query = models.Spot.objects.get(pk=pk)
        serializer = serializers.SpotSerializers(query, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostSpot(APIView):
    def post(self, request):
        serializer = serializers.SpotSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SearchSpot(APIView):
    def get(self, request):
        search = request.GET['name']
        query = models.Spot.objects.filter(name__contains=search)
        serializer = serializers.SpotSerializers(query, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class DeleteSpot(APIView):
    def delete(self, request, pk):
        query = models.Spot.objects.get(pk=pk)
        query.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
