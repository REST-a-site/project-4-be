from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from django.conf.urls import url
# from .views import CustomObtainAuthToken

urlpatterns = [
    path('api/fullmenu/<int:pk>', views.FullMenu.as_view()),
]
