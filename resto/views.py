from rest_framework import generics
from .serializers import MenuSerializer, MenuSectionSerializer
from .models import Menu, MenuSection, MenuItem
# Create your views here.

class Menu(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuSection(generics.ListCreateAPIView):
    queryset = MenuSection.objects.all()
    serializer_class = MenuSectionSerializer

# class MenuItem(generics.ListCreateAPIView):
#     queryset = MenuItem.objects.all()
#     serializer_class = MenuItemSerializer


