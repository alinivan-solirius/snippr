from django.forms import ModelForm, Select, Textarea, CharField
from snippets.models import Snippet, Language


# Create the form class.
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', "language", 'description']
        widgets = {
            'language': Select(),
            'description': Textarea(attrs={'rows': 15, 'overflow-y': 'scroll', 'maxlength': 10000}),
        }
