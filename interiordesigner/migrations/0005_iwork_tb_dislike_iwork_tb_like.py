# Generated by Django 4.1.4 on 2023-01-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiordesigner', '0004_iwork_tb_workvid'),
    ]

    operations = [
        migrations.AddField(
            model_name='iwork_tb',
            name='dislike',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='iwork_tb',
            name='like',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
