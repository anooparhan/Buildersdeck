# Generated by Django 4.1.2 on 2022-12-28 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contractor_tb',
            name='Email',
            field=models.EmailField(default='a@gmail.com', max_length=50),
        ),
    ]
