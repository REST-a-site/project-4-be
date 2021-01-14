from rest_framework import views
from .serializers import *
from .models import *
from rest_framework.response import Response
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# Create your views here.


class MenuView(views.APIView):
    def get_object(self, pk):
        try:
            return Menu.objects.get(pk=pk)
        except:
            raise Exception('Does not exist')

    def get(self, request, pk=None):
        if pk:
            menu = self.get_object(pk)
            serializer = MenuSerializer(menu)
            return Response(serializer.data)
        else:
            serializer = MenuSerializer(Menu.objects.all(), many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = MenuSerializer(request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk):
        menu = self.get_object(pk)
        serializer = MenuSerializer(menu, request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        menu = self.get_object(pk)
        return Response(menu.delete())


class MenuSectionView(views.APIView):
    def get_object(self, pk):
        try:
            return MenuSection.objects.get(pk=pk)
        except:
            raise Exception('Does not exist')

    def get(self, request, pk=None):
        if pk:
            menu_section = self.get_object(pk)
            serializer = MenuSectionSerializer(menu_section)
            return Response(serializer.data)
        else:
            serializer = MenuSectionSerializer(
                MenuSection.objects.all(), many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = MenuSectionSerializer(request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk):
        menu_section = self.get_object(pk)
        serializer = MenuSectionSerializer(menu_section, request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        MenuSection.objects.delete(pk=pk)


class MenuItemView(views.APIView):
    def get_object(self, pk):
        try:
            return MenuItem.objects.get(pk=pk)
        except:
            raise Exception('Does not exist')

    def get(self, request, pk=None):
        if pk:
            menu_item = self.get_object(pk)
            serializer = MenuItemSerializer(menu_item)
            return Response(serializer.data)
        else:
            serializer = MenuItemSerializer(MenuItem.objects.all(), many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = MenuItemSerializer(request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk):
        menu_item = self.get_object(pk)
        serializer = MenuItemSerializer(menu_item, request)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk):
        MenuItem.objects.delete(pk=pk)
