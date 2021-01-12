from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_name')


class MenuSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuSection
        fields = ('id', 'menu_section_name',
                  'menus')


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('id', 'menu_item_name', 'menu_item_description',
                  'menu_item_price', 'menu_section')
