# Generated by Django 3.0.4 on 2020-03-18 17:05

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0036_office_order_place_service_servicegroup'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='group',
        ),
        migrations.DeleteModel(
            name='ServiceGroup',
        ),
    ]
