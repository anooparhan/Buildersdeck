# Generated by Django 4.1.2 on 2023-01-31 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_sproduct_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='sproduct_tb',
            name='workvid',
            field=models.FileField(default='a.mp4', upload_to='swork_vid'),
        ),
    ]