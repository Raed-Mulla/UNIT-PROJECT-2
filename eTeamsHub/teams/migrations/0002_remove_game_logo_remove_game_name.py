# Generated by Django 5.2 on 2025-04-07 07:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='game',
            name='name',
        ),
    ]
