from rest_framework import serializers
from .models import Menu, MenuSection, MenuItem


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = ('id', 'menu_title', 'menu_description',
                  'active', 'menu_sections',)
        depth = 1


class MenuSectionSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuSection
        fields = ('id', 'section_title', 'section_description', 'menu_items')
        depth = 1


class MenuItemSerializer(serializers.HyperlinkedModelSerializer):
    menu = serializers.HyperlinkedRelatedField(
        view_name='menu_detail',
        read_only=True
    )

    class Meta:
        model = MenuItem
        fields = ('id', 'item_title', 'item_description',
                  'price', 'item_active')

# You can instantiate new properties in serializers that are not in the model/dictionary/object
