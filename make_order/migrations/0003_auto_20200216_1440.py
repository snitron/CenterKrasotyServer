# Generated by Django 3.0.3 on 2020-02-16 14:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0002_service_office'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(max_length=50),
        ),
    ]
