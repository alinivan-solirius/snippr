# Generated by Django 4.1.2 on 2022-10-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0002_language_alter_snippet_language'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='description',
            field=models.CharField(max_length=1000),
        ),
    ]
