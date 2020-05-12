# Generated by Django 3.0.4 on 2020-03-18 16:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('make_order', '0030_office_order_place_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='service',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='service',
            name='group_name',
        ),
        migrations.AddField(
            model_name='service',
            name='group',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='make_order.Group'),
        ),
    ]
