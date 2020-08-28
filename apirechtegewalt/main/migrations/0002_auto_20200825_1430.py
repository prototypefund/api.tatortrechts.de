# Generated by Django 3.1 on 2020-08-25 14:30

import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Incident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg_id', models.CharField(max_length=255)),
                ('url', models.CharField(max_length=255)),
                ('aggregator', models.CharField(max_length=255)),
                ('title', models.CharField(blank=True, default='', max_length=1000)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('iso3166_2', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg_id', models.CharField(max_length=255)),
                ('subdivisions', models.CharField(max_length=255)),
                ('location', django.contrib.gis.db.models.fields.PointField(default=django.contrib.gis.geos.point.Point(0.0, 0.0), geography=True, srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rg_id', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('url', models.CharField(blank=True, default='', max_length=255)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
