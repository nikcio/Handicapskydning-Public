# Generated by Django 2.2.7 on 2019-11-20 15:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0002_auto_20191120_1619'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 15, 20, 56, 872585, tzinfo=utc), verbose_name='Dato'),
        ),
    ]
