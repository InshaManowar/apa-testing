# Generated by Django 3.1.4 on 2021-06-18 14:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0021_auto_20210616_0904'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 18, 20, 25, 37, 319513)),
        ),
    ]