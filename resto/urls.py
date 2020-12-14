from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/menu', views.MenuList.as_view()),
    # path('api/menu/<int:pk>', views.MenuDetail.as_view(), name="menu_detail"),
    path('menu/<int:pk>', views.MenuDetail.as_view()),
    path('menu/', views.menu_list, name='menu')

    
    # path('api/menu_sections', views.MenuSectionList.as_view(), name='menu_sections_list'),
    # Menu is searching for a function in views.py
    # path('api/menu_sections/<int:pk>', views.MenuSectionDetail.as_view(), name='menu_sections_detail'),
    ## Menu_sections matches the serializers path view_name
    # path('menuitem/', views.MenuItem.as_view(), name='menu_item'),
    # path('menu/<int:pk>', views.Menu.as_view(), name='section_detail')
]