# Generated by Django 2.0.1 on 2018-07-23 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20180723_2233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='komiteer',
            old_name='description',
            new_name='post_description',
        ),
        migrations.RenameField(
            model_name='komiteer',
            old_name='image',
            new_name='post_image',
        ),
        migrations.RenameField(
            model_name='komiteer',
            old_name='title',
            new_name='post_title',
        ),
    ]