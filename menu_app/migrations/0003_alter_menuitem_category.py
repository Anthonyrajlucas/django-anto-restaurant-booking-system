# Generated by Django 3.2.21 on 2023-09-25 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0002_alter_menuitem_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='category',
            field=models.CharField(max_length=200),
        ),
    ]
