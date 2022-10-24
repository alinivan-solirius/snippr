from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect
from snippets.views import home, add_snippet, edit_snippet, delete_snippet

app_name = 'snippets'

urlpatterns = [
    path('', home, name='home'),
    path('add_snippet', add_snippet, name='add_snippet'),
    path('edit_snippet/<int:snippet_id>/', edit_snippet, name='edit_snippet'),
    path('delete_snippet/<int:snippet_id>/', delete_snippet, name='delete_snippet')
]