# Generated by Django 2.2.7 on 2019-11-24 15:02

import Handicapskydning.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0022_auto_20191121_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Navn')),
                ('file', models.FileField(upload_to=Handicapskydning.models.get_file)),
            ],
            options={
                'verbose_name': 'Dokument',
                'verbose_name_plural': 'Dokumenter',
            },
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 15, 2, 38, 146601, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 15, 2, 38, 145601, tzinfo=utc), verbose_name='Dato'),
        ),
    ]