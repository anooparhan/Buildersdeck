# Generated by Django 4.1.2 on 2023-02-26 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('astrologer', '0012_abook_tb_address_abook_tb_city_abook_tb_landmark_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astroleger_tb',
            name='Pincode',
            field=models.IntegerField(max_length=6),
        ),
    ]
