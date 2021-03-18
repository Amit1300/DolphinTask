from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from api.serializer import Usersserializer
from rest_framework import status
from django.http import Http404
from django.contrib.auth.models import User
from .models import *
from django.core.paginator import Paginator
# Create your views here.
class UserApi(APIView):

    def get(self, request):
        users=Users.objects.all()
        paginator = Paginator(users, 10)
        serializer =Usersserializer(users, many=True)
        return Response(serializer.data)
        

    def post(self, request, format=None):
        serializer =Usersserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):

        user=Users.objects.get(pk=pk)
        print(user)
        if user:
            serializer =Usersserializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
    