# Generated by Django 3.0.3 on 2021-03-31 14:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_auto_20210331_2011'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='display_picture',
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 20, 14, 22, 567518)),
        ),
    ]