# Generated by Django 2.2.2 on 2020-07-17 11:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='day',
            field=models.CharField(default=datetime.datetime(2020, 7, 17, 11, 29, 22, 140590, tzinfo=utc), max_length=3),
        ),
    ]
