# Generated by Django 2.1.3 on 2018-12-14 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField(blank=True)),
                ('image_path', models.ImageField()),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('rgb16', models.CharField(max_length=7)),
                ('code_color', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en', models.CharField(max_length=5)),
                ('ru_min', models.PositiveSmallIntegerField()),
                ('ru_max', models.PositiveSmallIntegerField()),
                ('text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('mainInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='torien.BaseItem')),
                ('date_start', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Thing',
            fields=[
                ('mainInfo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='torien.BaseItem')),
                ('cost', models.PositiveIntegerField()),
                ('material', models.CharField(max_length=25)),
                ('color', models.ManyToManyField(to='torien.Color')),
                ('size', models.ManyToManyField(to='torien.Size')),
            ],
        ),
    ]
