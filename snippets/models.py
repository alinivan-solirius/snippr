from django.db import models

# Create your models here.
from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=50)


class Snippet(models.Model):
    """
    langs = (
        (1, 'Python'),
        (2, 'Java'),
        (3, 'JavaScript')
    )
    """

    title = models.CharField(max_length=100)
    language = models.ForeignKey(Language, on_delete=models.PROTECT)
    description = models.CharField(max_length=1000)

