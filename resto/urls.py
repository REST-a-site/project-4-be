from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
# from .views import CustomObtainAuthToken

urlpatterns = [
    path('api/menu', views.MenuList.as_view()),
    path('api/items/<int:pk>', views.MenuDetail.as_view()),
]
