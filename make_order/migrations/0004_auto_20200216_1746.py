# Generated by Django 3.0.3 on 2020-02-16 17:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0003_auto_20200216_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedule',
            name='place',
        ),
        migrations.RemoveField(
            model_name='sp',
            name='place',
        ),
        migrations.AddField(
            model_name='order',
            name='finish_time',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.AddField(
            model_name='order',
            name='start_time',
            field=models.CharField(default='0', max_length=30),
        ),
        migrations.DeleteModel(
            name='OrderTime',
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
        migrations.DeleteModel(
            name='SP',
        ),
    ]
