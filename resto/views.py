from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from .models import *
# Create your views here.


class MenuList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# class MenuSectionList(generics.ListCreateAPIView):
#     queryset = MenuSection.objects.all()
#     serializer_class = MenuSectionSerializer


# class MenuSectionDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = MenuSection.objects.all()
#     serializer_class = MenuSectionSerializer

# class MenuItem(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer

def menu_list(request):
    menus = Menu.objects.all()
    return render (request, 'resto/menu.html', {'menus': menus})