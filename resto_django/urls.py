from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resto.urls')),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

    # path('users/', include('users.urls')),
]
