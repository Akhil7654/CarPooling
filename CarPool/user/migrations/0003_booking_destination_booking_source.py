# Generated by Django 4.1.4 on 2023-02-01 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_booking_seat'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='destination',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='booking',
            name='source',
            field=models.CharField(default='', max_length=100),
        ),
    ]
