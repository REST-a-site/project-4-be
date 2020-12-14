from rest_framework import serializers
from .models import *


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ('id', 'menu_name', 'menu_description',
                  'active', 'menu_item_names')
        depth = 2


# class MenuSectionSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = MenuSection
#         fields = ('id', 'section_name', 'section_description', 'menu_items')
#         depth = 1


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

# You can instantiate new properties in serializers that are not in the model/dictionary/object
