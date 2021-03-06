# Generated by Django 2.2.2 on 2019-07-22 16:12

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Komite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', imagekit.models.fields.ProcessedImageField(upload_to='komite/')),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TheSign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500)),
                ('edition', models.CharField(choices=[('1. utgave', '1. utgave'), ('2. utgave', '2. utgave'), ('3. utgave', '3. utgave'), ('4. utgave', '4. utgave'), ('5. utgave', '5. utgave')], max_length=20)),
            ],
        ),
    ]
