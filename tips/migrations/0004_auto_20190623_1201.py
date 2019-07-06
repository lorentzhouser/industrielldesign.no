# Generated by Django 2.2.2 on 2019-06-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tips', '0003_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='tip',
        ),
        migrations.AddField(
            model_name='tip',
            name='tags',
            field=models.ManyToManyField(to='tips.Tag'),
        ),
    ]
