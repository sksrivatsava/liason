# Generated by Django 3.0.3 on 2021-03-31 14:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20210331_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='display_picture',
            field=models.ImageField(blank=True, default='display_pictures/default_nice.jpg', upload_to='display_pictures/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 31, 20, 11, 57, 441861)),
        ),
    ]
