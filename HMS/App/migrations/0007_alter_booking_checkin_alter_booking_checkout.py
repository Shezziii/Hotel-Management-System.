# Generated by Django 4.1 on 2022-10-12 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_rename_leave_at_booking_checkin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='CheckIn',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='CheckOut',
            field=models.DateField(auto_now=True),
        ),
    ]