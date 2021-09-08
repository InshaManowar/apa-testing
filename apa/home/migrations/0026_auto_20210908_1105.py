# Generated by Django 3.1.4 on 2021-09-08 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20210828_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='videosidebar',
            name='subtitle',
            field=models.TextField(blank=True, default=None),
        ),
        migrations.AlterField(
            model_name='video',
            name='created_time',
            field=models.DateTimeField(default=datetime.datetime(2021, 9, 8, 11, 5, 27, 413947)),
        ),
        migrations.AlterField(
            model_name='videodisplay',
            name='display',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='videosidebar',
            name='display_sidebar',
            field=models.CharField(blank=True, default=None, max_length=255),
        ),
    ]