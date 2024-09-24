# Generated by Django 4.1.2 on 2023-02-04 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0008_ecomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='EBook_TB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Email', models.EmailField(default='a@gmail.com', max_length=50)),
                ('Number', models.CharField(max_length=50)),
                ('astroid', models.CharField(default='1', max_length=100)),
                ('userid', models.CharField(max_length=50)),
                ('location', models.CharField(default=0, max_length=50)),
                ('time', models.CharField(default=0, max_length=20)),
                ('date', models.CharField(default=0, max_length=20)),
                ('accept', models.BooleanField(default='False')),
                ('reject', models.BooleanField(default='False')),
                ('fees', models.CharField(default='0', max_length=20)),
            ],
        ),
    ]
