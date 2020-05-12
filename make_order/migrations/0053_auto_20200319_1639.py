# Generated by Django 3.0.4 on 2020-03-19 16:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0052_service_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='service',
        ),
        migrations.AddField(
            model_name='order',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='make_order.ServiceGroup'),
        ),
        migrations.AddField(
            model_name='place',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE,
                                    to='make_order.ServiceGroup'),
        ),
    ]
