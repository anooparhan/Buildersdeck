# Generated by Django 4.1.4 on 2023-01-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interiordesigner', '0003_iwork_tb'),
    ]

    operations = [
        migrations.AddField(
            model_name='iwork_tb',
            name='workvid',
            field=models.FileField(default='a.mp4', upload_to='cwork_vid'),
        ),
    ]