# Generated by Django 3.2.21 on 2023-09-26 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_alter_booking_total_tables'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='start_time',
        ),
        migrations.AddField(
            model_name='booking',
            name='booking_time',
            field=models.CharField(choices=[('10:00', '10:00 AM'), ('11:00', '11:00 AM'), ('12:00', '12:00 PM'), ('13:00', '01:00 PM'), ('14:00', '02:00 PM'), ('15:00', '03:00 PM'), ('16:00', '04:00 PM'), ('17:00', '05:00 PM'), ('18:00', '06:00 PM'), ('19:00', '07:00 PM'), ('20:00', '08:00 PM'), ('21:00', '09:00 PM'), ('22:00', '10:00 PM')], default='10:00', max_length=5),
        ),
    ]