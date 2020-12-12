from rest_framework import serializers
from .models import Menu, MenuSection, MenuItem


class MenuSerializer(serializers.HyperlinkedModelSerializer):
    menu_sections = serializers.HyperlinkedRelatedField(
        view_name='menu_sections_detail',
        many=True,
        read_only=True
    )

    menu_url = serializers.ModelSerializer.serializer_url_field(
        view_name='menu_detail'
    )

    class Meta:
        model = Menu
        fields = ('id', 'menu_title', 'menu_description',
                  'active', 'menu_sections', 'menu_url')


class MenuSectionSerializer(serializers.HyperlinkedModelSerializer):
    menu = serializers.HyperlinkedRelatedField(
        view_name='menu_detail',
        read_only=True
    )

    menu_id = serializers.PrimaryKeyRelatedField(
        queryset=Menu.objects.all(),
        source='menu'
    )

    class Meta:
        model = MenuSection
        fields = ('id', 'section_title',
                  'section_description', 'menu', 'menu_id')


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
