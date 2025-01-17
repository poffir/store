# Generated by Django 5.1.4 on 2025-01-17 18:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpu_name', models.CharField(max_length=200)),
                ('cpu_core', models.IntegerField(default=2)),
                ('cpu_video_core', models.IntegerField(default=0)),
                ('cpu_frequency', models.DecimalField(decimal_places=2, default=1, max_digits=10)),
                ('streams', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gpu_name', models.CharField(max_length=200)),
                ('gpu_core', models.IntegerField(default=2)),
                ('gpu_memory', models.IntegerField(default=2)),
                ('gpu_frequency', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='RAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ram_name', models.CharField(max_length=200)),
                ('ram_size', models.IntegerField(default=2)),
                ('ram_frequency', models.IntegerField(default=2)),
            ],
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssd_name', models.CharField(max_length=200)),
                ('ssd_size', models.IntegerField(default=2)),
                ('ssd_speed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
                ('slug', models.SlugField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='main_catego_name_5111b9_idx')],
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_created=True)),
                ('created', models.DateTimeField(auto_created=True)),
                ('name', models.CharField(max_length=40)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(max_length=4000)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('variable', models.BooleanField(default=True)),
                ('discount', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Characteristics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hz', models.DecimalField(decimal_places=2, max_digits=10)),
                ('resolution', models.DecimalField(decimal_places=2, max_digits=10)),
                ('weight', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('settings', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.category')),
                ('cpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cpu')),
                ('gpu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.gpu')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ram')),
                ('ssd', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ssd')),
            ],
        ),
    ]
