from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('/', views.index),
    path('main/', views.main),
    # встроенная админка
    path('admin/', admin.site.urls),
    path('logout/', views.main, name="main"),
]
