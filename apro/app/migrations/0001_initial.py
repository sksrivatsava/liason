# Generated by Django 3.0.3 on 2021-01-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(default='', max_length=50)),
                ('username', models.CharField(default='', max_length=50)),
                ('department', models.CharField(default='', max_length=50)),
                ('designation', models.CharField(default='', max_length=50)),
                ('foll', models.CharField(default='', max_length=5000)),
            ],
        ),
    ]
