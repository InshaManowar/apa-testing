# Generated by Django 3.1.4 on 2021-06-11 17:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20210611_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 11, 22, 37, 39, 935391)),
        ),
    ]