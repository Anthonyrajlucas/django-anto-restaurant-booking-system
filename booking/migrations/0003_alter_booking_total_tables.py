# Generated by Django 3.2.21 on 2023-09-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0002_booking_total_tables'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='total_tables',
            field=models.PositiveIntegerField(),
        ),
    ]
