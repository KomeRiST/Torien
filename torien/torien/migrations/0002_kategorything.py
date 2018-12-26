# Generated by Django 2.1.3 on 2018-12-15 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('torien', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='KategoryThing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('things', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='torien.Thing')),
            ],
        ),
    ]