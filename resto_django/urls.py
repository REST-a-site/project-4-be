from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('resto.urls')),
    path('users/', include('django.contrib.auth.urls')),
    #^ Pointing to our users directory. django.contrib.auth is the django authentification system, it has a package called URLS that will take care of login, logout, etc... urls.
    path('users/', include('users.urls')),
    # ^ Here we have two URL's pointing to the same place. The order is important because django willuse the auth urls and then if it see's something else
    # it needs to know where to go. 
     
     
    # path('api-auth', include('rest_framework.urls', namespace='rest_framework')),

]
