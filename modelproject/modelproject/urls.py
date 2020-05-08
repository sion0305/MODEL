from django.contrib import admin
from django.urls import path
import blog.views

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path("", blog.views.home, name="home")
]
