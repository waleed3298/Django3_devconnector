# Generated by Django 3.0.5 on 2020-06-13 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0031_auto_20200613_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(blank=True, default='devconnector/images/nopic1.png', null=True, upload_to='media/devconnector/images'),
        ),
    ]
