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


# class FullMenuSerializer(serializers.ModelSerializer):
#     menu_id = MenuSerializer(read_only=True)
#     menu_section_id = MenuSectionSerializer(many=True)
#     menu_item_id = MenuItemSerializer(many=True)

#     class Meta:
#         model = FullMenu
#         fields = ('id', 'menu_id', 'menu_section_id', 'menu_item_id')
