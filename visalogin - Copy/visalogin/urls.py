from django.contrib import admin
from django.urls import path
from login.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register',register),
    path('login',check),
    path('',Main),
    path('',check),
    path('',show),

]
