# Generated by Django 3.1.4 on 2021-09-23 06:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0028_auto_20210908_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 23, 12, 27, 59, 525363)),
        ),
    ]
