# Generated by Django 4.1.4 on 2023-01-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0010_alter_cwork_tb_dislike_alter_cwork_tb_like'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cwork_tb',
            name='dislike',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='cwork_tb',
            name='like',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
