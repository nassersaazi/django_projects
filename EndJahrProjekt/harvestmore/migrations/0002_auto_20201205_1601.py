# Generated by Django 2.2.6 on 2020-12-05 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('harvestmore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='path',
            field=models.ImageField(default='default.jpg', upload_to='cassava_images'),
        ),
    ]