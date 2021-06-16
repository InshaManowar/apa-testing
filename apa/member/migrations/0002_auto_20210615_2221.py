# Generated by Django 3.1.4 on 2021-06-15 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='college',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='council_reg_no',
            field=models.CharField(default='a-00000-b-1', max_length=12),
        ),
        migrations.AlterField(
            model_name='member',
            name='dob',
            field=models.DateField(default='yyyy-mm-dd'),
        ),
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile2',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='mobile3',
            field=models.CharField(blank=True, default='', max_length=10, null=True),
        ),
    ]