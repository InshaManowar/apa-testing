# Generated by Django 3.1.4 on 2021-06-08 19:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210506_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 9, 1, 12, 56, 149302)),
        ),
    ]