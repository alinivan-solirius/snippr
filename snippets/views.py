from django.http import HttpResponse

from django.shortcuts import render, redirect

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
        return redirect('snippets:home')
    else:
        snippet_form = SnippetForm()
    return render(request, 'new_snippet.html', {
        "snippet_form": snippet_form
    })


def edit_snippet(request, snippet_id=None):
    snippet = Snippet.objects.get(id=snippet_id)
    languages = Language.objects.all()

    if request.method == "POST":
        snippet_form = SnippetForm(request.POST, instance=snippet)
        snippet_form.save()
        return redirect('snippets:home')
    else:
        print(languages)
        snippet_form = SnippetForm(instance=snippet)
    return render(request, 'edit_snippet.html', {
        "snippet_form": snippet_form,
        "languages": languages
    })


def delete_snippet(request, snippet_id=None):
    snippet = Snippet.objects.get(id=snippet_id)
    if request.method == "GET":
        snippet.delete()
    return render(request, 'delete_snippet.html', {
        "snippet": snippet
    })