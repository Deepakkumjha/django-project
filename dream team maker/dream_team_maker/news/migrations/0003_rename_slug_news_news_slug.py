# Generated by Django 4.2.4 on 2024-02-10 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_news_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='slug',
            new_name='news_slug',
        ),
    ]
