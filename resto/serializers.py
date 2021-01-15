from rest_framework import serializers
from .models import *


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = ('id', 'menu_item_name', 'menu_item_description',
                  'menu_item_price')


class MenuSectionSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True)

    class Meta:
        model = MenuSection
        fields = ('id', 'menu_section_name',
                  'menu_section_alias', 'menu_items')


class MenuSerializer(serializers.ModelSerializer):
    menu_section_name = MenuSectionSerializer(many=True)
    menu_section_alias = MenuSectionSerializer(read_only=True)

    class Meta:
        model = Menu
        fields = ('id', 'menu_name', 'menu_section_name', 'menu_section_alias')
