from rest_framework import generics
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
