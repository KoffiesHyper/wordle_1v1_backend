# Generated by Django 3.2.9 on 2022-06-29 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordle', '0002_auto_20220628_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='match',
            name='has_started',
            field=models.BooleanField(default=False),
        ),
    ]
