# Generated by Django 4.1.4 on 2023-01-21 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrologer', '0006_abook_tb_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='abook_tb',
            name='location',
            field=models.CharField(default=0, max_length=50),
        ),
    ]
