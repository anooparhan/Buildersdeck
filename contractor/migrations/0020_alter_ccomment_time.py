# Generated by Django 4.1.4 on 2023-01-27 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0019_ccomment_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccomment',
            name='time',
            field=models.DateTimeField(null='True'),
        ),
    ]