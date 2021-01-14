from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_name')


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('id', 'menu_item_name', 'menu_item_description',
                  'menu_item_price')


class MenuSectionSerializer(serializers.ModelSerializer):
    menus = MenuSerializer(many=True)
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = MenuSection
        fields = ('id', 'menu_section_name',
                  'menus', 'menu_items')

