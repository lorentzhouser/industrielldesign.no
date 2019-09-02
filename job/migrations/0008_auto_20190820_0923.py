# Generated by Django 2.2.2 on 2019-08-20 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20190819_1957'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name': 'Bedrift', 'verbose_name_plural': 'Bedrifter'},
        ),
        migrations.AddField(
            model_name='job',
            name='filters',
            field=models.ManyToManyField(to='job.JobFilter'),
        ),
    ]