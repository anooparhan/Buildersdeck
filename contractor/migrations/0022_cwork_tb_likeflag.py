# Generated by Django 4.1.2 on 2023-02-18 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0021_cbook_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='cwork_tb',
            name='likeflag',
            field=models.BooleanField(default='False'),
        ),
    ]
