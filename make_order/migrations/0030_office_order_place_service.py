# Generated by Django 3.0.4 on 2020-03-18 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('make_order', '0029_auto_20200318_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Office',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('info', models.TextField()),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('geo_coords', models.CharField(max_length=50)),
                ('st_time', models.CharField(default='08:00', max_length=40)),
                ('fin_time', models.CharField(default='18:00', max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField(default=0)),
                ('group_name', models.CharField(default='0', max_length=20)),
                ('name', models.CharField(max_length=30)),
                ('info', models.TextField(default='.')),
                ('price', models.FloatField(default=0.0)),
                ('long', models.IntegerField(default=60)),
                ('office',
                 models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='make_order.Office')),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('info', models.TextField()),
                ('image', models.ImageField(upload_to='usr/share/django-projects/welcome/static/images/')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='make_order.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('login', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=15)),
                ('start_time', models.CharField(default='0', max_length=30)),
                ('finish_time', models.CharField(default='0', max_length=30)),
                ('group_id', models.IntegerField(default=0)),
                ('place',
                 models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='make_order.Place')),
            ],
        ),
    ]
