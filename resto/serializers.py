from rest_framework import serializers
from .models import *

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = ('id', 'menu_section', 'item_name', 'item_description',
                  'price', 'item_active')
        depth = 2

class FullMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = FullMenu
        fields = ('id', 'section_name', 'menu_item' )
        depth = 2