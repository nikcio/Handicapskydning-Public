# Generated by Django 2.2.7 on 2019-11-20 17:39

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Handicapskydning', '0010_auto_20191120_1818'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Afdeling')),
            ],
            options={
                'verbose_name': 'Bestyrelse',
                'verbose_name_plural': 'Bestyrelser',
            },
        ),
        migrations.AlterField(
            model_name='activity',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 17, 39, 28, 809976, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 11, 20, 17, 39, 28, 809976, tzinfo=utc), verbose_name='Dato'),
        ),
        migrations.AlterField(
            model_name='results',
            name='link',
            field=models.URLField(max_length=2083, verbose_name='Link'),
        ),
        migrations.CreateModel(
            name='StaffMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Navn')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('phone', models.PositiveIntegerField(verbose_name='Tlf')),
                ('address', models.CharField(max_length=255, verbose_name='Adresse')),
                ('city', models.CharField(max_length=255, verbose_name='By')),
                ('postal_code', models.PositiveSmallIntegerField(verbose_name='Post nummer')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Handicapskydning.Department')),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Personer',
            },
        ),
    ]
