# Generated by Django 2.2.7 on 2019-11-24 17:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0032_auto_20191124_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 17, 18, 32, 839461, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 17, 18, 32, 839461, tzinfo=utc), verbose_name='Dato'),
        ),
    ]