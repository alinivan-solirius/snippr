from django.contrib import admin
from django.urls import path, include
from snippets.views import home, add_snippet


urlpatterns = [
    path('', home),
    path('add_snippet', add_snippet),
]