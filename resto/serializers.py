from rest_framework import serializers
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_type',
                  'active', 'menu_item_name')
        depth = 2

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    menu = MenuSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = MenuItem
        fields = ('id', 'item_name', 'item_description',
                  'price', 'item_active', 'menu_section', 'menu')
        depth = 2

