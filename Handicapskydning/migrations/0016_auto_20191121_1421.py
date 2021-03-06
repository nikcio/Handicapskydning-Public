# Generated by Django 2.2.7 on 2019-11-21 13:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0015_auto_20191120_2048'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staffmember',
            old_name='staff',
            new_name='department',
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 21, 13, 21, 5, 897958, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 21, 13, 21, 5, 897958, tzinfo=utc), verbose_name='Dato'),
        ),
    ]
