# Generated by Django 3.0.4 on 2020-03-19 16:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0049_auto_20200319_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='make_order.ServiceGroup'),
        ),
    ]
