# Generated by Django 4.2.4 on 2024-02-15 20:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactus', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
    ]