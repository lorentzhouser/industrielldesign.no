# Generated by Django 2.0.1 on 2018-09-06 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0003_auto_20180906_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='graduation_year',
            field=models.IntegerField(choices=[(2023, '1.klasse'), (2022, '2.klasse'), (2021, '3.klasse'), (2020, '4.klasse'), (2019, '5.klasse'), (1, 'Alumni')], verbose_name='Klasse'),
        ),
    ]