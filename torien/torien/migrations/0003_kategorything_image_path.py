# Generated by Django 2.1.3 on 2018-12-15 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('torien', '0002_kategorything'),
    ]

    operations = [
        migrations.AddField(
            model_name='kategorything',
            name='image_path',
            field=models.ImageField(default='IconsThings/images/icondefault.jpg', upload_to='IconsThings/images'),
            preserve_default=False,
        ),
    ]
