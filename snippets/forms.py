from django.forms import ModelForm, ChoiceField, Textarea
from snippets.models import Snippet, Language


# Create the form class.
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'language', 'description']

        widgets = {
            'description': Textarea(attrs={'rows': 30}),
        }