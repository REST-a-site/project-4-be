from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class MenuList(generics.ListCreateAPIView):
    queryset = FullMenu.objects.all()
    serializer_class = FullMenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class FullMenu(generics.RetrieveUpdateDestroyAPIView):
    queryset = FullMenu.objects.all()
    serializer_class = FullMenuSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
