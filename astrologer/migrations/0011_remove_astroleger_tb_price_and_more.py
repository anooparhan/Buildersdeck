# Generated by Django 4.1.2 on 2023-01-31 15:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('astrologer', '0010_abook_tb_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='astroleger_tb',
            name='Price',
        ),
        migrations.RemoveField(
            model_name='astroleger_tb',
            name='Travelling',
        ),
    ]
