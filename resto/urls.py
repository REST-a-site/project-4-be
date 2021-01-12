from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
# from .views import CustomObtainAuthToken
urlpatterns = [
    path('api/menus', views.MenuView.as_view()),
    path('api/menus/<int:pk>', views.MenuView.as_view()),
    path('api/sections', views.MenuItemView.as_view()),
    path('api/sections/<int:pk>', views.MenuSectionView.as_view()),
    path('api/items', views.MenuItemView.as_view()),
    path('api/items/<int:pk>', views.MenuItemView.as_view()),
]
