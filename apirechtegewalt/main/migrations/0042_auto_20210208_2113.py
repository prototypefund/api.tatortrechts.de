# Generated by Django 3.1.5 on 2021-02-08 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0041_auto_20210207_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='latitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='location',
            name='longitude',
            field=models.FloatField(default=1),
            preserve_default=False,
        ),
    ]
