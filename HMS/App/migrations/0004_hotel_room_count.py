# Generated by Django 4.1 on 2022-09-29 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='room_count',
            field=models.IntegerField(default=10),
        ),
    ]
