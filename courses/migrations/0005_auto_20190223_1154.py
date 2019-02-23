# Generated by Django 2.0.1 on 2019-02-23 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_course_class_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('url_title', models.CharField(max_length=500)),
                ('url_description', models.TextField()),
                ('img_url', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='links',
            field=models.ManyToManyField(to='courses.CourseLink'),
        ),
    ]
