from django.contrib import admin
from django.urls import path, include
from snippets.views import base


urlpatterns = [
    path('', base),
]