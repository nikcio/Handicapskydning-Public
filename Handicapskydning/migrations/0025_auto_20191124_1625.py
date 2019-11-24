# Generated by Django 2.2.7 on 2019-11-24 15:25

import Handicapskydning.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0024_auto_20191124_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lane',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(upload_to=Handicapskydning.models.get_lane_picture)),
            ],
            options={
                'verbose_name': 'Bane billede',
                'verbose_name_plural': 'Bane billeder',
            },
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 15, 25, 38, 739668, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 15, 25, 38, 739668, tzinfo=utc), verbose_name='Dato'),
        ),
    ]
