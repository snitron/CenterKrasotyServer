# Generated by Django 3.0.4 on 2020-03-17 15:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0013_auto_20200317_1531'),
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
