# Generated by Django 3.0.3 on 2021-01-09 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210109_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='followers',
            field=models.CharField(default='', max_length=5000),
        ),
    ]
