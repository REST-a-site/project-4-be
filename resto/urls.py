from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('api/menu', views.Menu.as_view()),
    path('api/menusections', views.MenuSection.as_view()),
    # Menu is searching for a function in views.py
    path('api/menusections/<int:pk>', views.MenuSection.as_view(), name='menu_detail'),
    ## Menu_sections matches the serializers path view_name
    # path('menuitem/', views.MenuItem.as_view(), name='menu_item'),
    # path('menu/<int:pk>', views.Menu.as_view(), name='section_detail')
]