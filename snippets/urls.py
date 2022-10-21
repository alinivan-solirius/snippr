from django.contrib import admin
from django.urls import path, include
from snippets.views import home, add_snippet, edit_snippet


urlpatterns = [
    path('', home),
    path('add_snippet', add_snippet, name='add_snippet'),
    path('edit_snippet/<int:snippet_id>/', edit_snippet, name='edit_snippet')
]