from rest_framework import generics
from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
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
    jeff = Menu.objects.all()
    # print(jeff)
    return render(request, 'resto/menu_list.html', {'menus': jeff})

    # on line 33 the string is the key and menus is the object
    # The actual data object is the second argument on 34, which matches the varibale for the objects.all()


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(
            request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        return Response({'token': token.key, 'id': token.user_id})
