# Generated by Django 3.0.4 on 2020-03-17 17:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0020_auto_20200317_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]