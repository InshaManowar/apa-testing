# Generated by Django 3.1.4 on 2021-03-15 03:41

from django.db import migrations, models
import django.db.models.deletion
import events.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(blank=True, max_length=200, unique=True)),
                ('location', models.CharField(max_length=100)),
                ('content', models.TextField(default='')),
                ('subtitle', models.TextField(default='')),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField(default='')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
            ],
            options={
                'ordering': ['startdate'],
            },
        ),
        migrations.CreateModel(
            name='EventTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date_for_day', models.DateTimeField()),
                ('end_date_for_day', models.DateTimeField()),
                ('title_for_day', models.CharField(default='', max_length=100)),
                ('description_for_day', models.TextField(default='')),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_of_event', models.CharField(default='', max_length=120)),
                ('short_description', models.TextField(default='', max_length=150)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
        migrations.CreateModel(
            name='EventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, default=None, upload_to=events.models.upload_location)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='events.event')),
            ],
        ),
    ]