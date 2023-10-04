from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ping/', views.pingpong ),
    path('index/', views.index),
    path('getdata/', views.getdata),
    path('todo/', include('todo.urls')),

]
