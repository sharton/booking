# Generated by Django 2.0.4 on 2018-05-08 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='car',
        ),
    ]
