# Generated by Django 2.0.1 on 2018-09-13 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_remove_event_open_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='registration_year_limit',
            field=models.IntegerField(blank=True, choices=[(5000, 'Alle (inkludert alumni)'), (2023, '1. - 5. klasse'), (2022, '2. - 5. klasse'), (2021, '3. - 5. klasse'), (2020, '4. og 5. klasse'), (2019, '5. klasse')], null=True, verbose_name='Åpent for:'),
        ),
    ]