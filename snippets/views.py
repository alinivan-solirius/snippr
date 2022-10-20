from django.http import HttpResponse

from django.shortcuts import render

from snippets.formatter import Formatter
from snippets.models import Snippet
from snippets.models import Language
from django.template import loader
from snippets.forms import SnippetForm

# Create your views here.


def home(request):
    snippets = Snippet.objects.all()
    for snip in snippets:
        code = Formatter(code=snip.description, lexer=snip.language.title.lower())
        formatted_code = code.format_code()
        if "Internal Server Error" not in formatted_code:
            snip.description = formatted_code
    return render(request, 'home.html', {
        "snippets": snippets
    })


def add_snippet(request):
    if request.method == "POST":
        snippet_form = SnippetForm(request.POST)
        snippet_form.save()
    else:
        snippet_form = SnippetForm()
    return render(request, 'new_snippet.html', {
        "snippet_form": snippet_form
    })