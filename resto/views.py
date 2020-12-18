from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.

class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]

class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    permission_classes=[IsAuthenticatedOrReadOnly]