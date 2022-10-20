from django.forms import ModelForm, ChoiceField
from snippets.models import Snippet, Language


# Create the form class.
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', 'language', 'description']