# Generated by Django 3.1.4 on 2021-06-15 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20210615_2221'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='female',
        ),
        migrations.RemoveField(
            model_name='member',
            name='male',
        ),
        migrations.AddField(
            model_name='member',
            name='gender',
            field=models.IntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'not specified')], default=None),
        ),
    ]