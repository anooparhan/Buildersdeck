# Generated by Django 4.1.2 on 2022-12-29 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interiordesigner', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='designer_tb',
            name='Password',
        ),
    ]
