from django.db import models

# Create your models here.
from django.db import models


class Language(models.Model):
    title = models.CharField(max_length=50)


class Snippet(models.Model):
    title = models.CharField(max_length=100)
    language = models.ForeignKey(
        to=Language,
        related_name="language",
        on_delete=models.PROTECT
    )
    description = models.CharField(max_length=10000)

