# Generated by Django 2.2.7 on 2019-11-24 17:34

import Handicapskydning.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0033_auto_20191124_1818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='results',
            name='link',
        ),
        migrations.AddField(
            model_name='results',
            name='file',
            field=models.FileField(default='static/Results/placegoler.png', upload_to=Handicapskydning.models.get_file_results, verbose_name='fil'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 17, 32, 15, 456854, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 17, 32, 15, 456854, tzinfo=utc), verbose_name='Dato'),
        ),
    ]
