# Generated by Django 2.2.7 on 2019-11-24 16:36

import Handicapskydning.models
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0028_auto_20191124_1730'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collections',
            options={'verbose_name': 'Samling', 'verbose_name_plural': 'Samlinger'},
        ),
        migrations.AlterModelOptions(
            name='cpictures',
            options={'verbose_name': 'Billede', 'verbose_name_plural': 'Billeder'},
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 16, 36, 49, 253145, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='cpictures',
            name='picture',
            field=models.ImageField(upload_to=Handicapskydning.models.get_collection_image, verbose_name='Billede'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 24, 16, 36, 49, 252145, tzinfo=utc), verbose_name='Dato'),
        ),
    ]
