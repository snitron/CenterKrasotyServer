# Generated by Django 3.0.4 on 2020-03-17 17:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0024_auto_20200317_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]