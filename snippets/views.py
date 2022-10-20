from django.http import HttpResponse

from django.shortcuts import render

from snippets.formatter import Formatter
from snippets.models import Snippet
from django.template import loader


# Create your views here.


def base(request):
    snippets = Snippet.objects.all()
    for snip in snippets:
        code = Formatter(code=snip.description, lexer="python")
        snip.description = code.format_code()
    return render(request, 'base.html', {
        "snippets": snippets
    })

