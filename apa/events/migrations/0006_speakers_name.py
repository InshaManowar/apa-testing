# Generated by Django 3.1.4 on 2021-09-23 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_speakers'),
    ]

    operations = [
        migrations.AddField(
            model_name='speakers',
            name='name',
            field=models.CharField(default='', max_length=255),
        ),
    ]
