# Generated by Django 4.1.2 on 2022-12-29 06:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop_tb',
            name='Password',
        ),
    ]
