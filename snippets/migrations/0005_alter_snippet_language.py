# Generated by Django 4.1.2 on 2022-10-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0004_alter_language_title_alter_snippet_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='language',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='snippets.language'),
        ),
    ]
