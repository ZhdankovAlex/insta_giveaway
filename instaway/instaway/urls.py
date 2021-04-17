from django.contrib import admin
from django.urls import path, re_path, include
from core import views

urlpatterns = [
    re_path(r'^authorized/link_parse/', views.link_parse, name="link_parse"),
    re_path(r'^authorized/progress_bar/', views.progress_bar, name="progress_bar"),
    re_path(r'^authorized/results/', views.results, name="results"),
    re_path(r'^authorized/', views.authorized, name="authorized"),
    re_path(r'^$', views.main, name="main"),
    # встроенная админка
    path('admin/', admin.site.urls),
    path('logout/', views.main, name="main"),
]
