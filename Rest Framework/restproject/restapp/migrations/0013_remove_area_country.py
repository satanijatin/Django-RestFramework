# Generated by Django 5.0.3 on 2024-04-04 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0012_area_country'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='country',
        ),
    ]
