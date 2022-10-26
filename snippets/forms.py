from django.forms import ModelForm, Select, Textarea, ModelMultipleChoiceField
from snippets.models import Snippet, Language


# class CustomLanguageTitle(ModelMultipleChoiceField):
#     def label_from_instance(self, language):
#         return language


# Create the form class.
class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        fields = ['title', "language", 'description']
        widgets = {
            'language': Select(),
            'description': Textarea(attrs={'rows': 30}),
        }

    # language = CustomLanguageTitle(
    #     queryset = Language.objects.all(),
    #     widget = Select
    # )