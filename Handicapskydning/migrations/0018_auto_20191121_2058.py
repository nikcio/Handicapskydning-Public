# Generated by Django 2.2.7 on 2019-11-21 19:58

import Handicapskydning.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0017_auto_20191121_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='staffmember',
            name='profile_image',
            field=models.ImageField(default='static/assets/images/mbr-510x510.jpg', upload_to=Handicapskydning.models.get_profile_picture),
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 21, 19, 58, 53, 181983, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 21, 19, 58, 53, 181983, tzinfo=utc), verbose_name='Dato'),
        ),
    ]
