from rest_framework import serializers
from .models import *

class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_name', 'menu_description',
                  'active', 'menu_item_names')
        depth = 2

class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    menu = MenuSerializer(
        many=True,
        read_only=True
    )

    class Meta:
        model = MenuItem
        fields = ('id', 'item_title', 'item_description',
                  'price', 'item_active')
        depth = 2

