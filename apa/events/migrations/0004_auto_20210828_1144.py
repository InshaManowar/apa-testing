# Generated by Django 3.1.4 on 2021-08-28 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_event_link'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['-startdate']},
        ),
    ]
