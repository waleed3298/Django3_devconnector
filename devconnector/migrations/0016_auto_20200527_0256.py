# Generated by Django 3.0.5 on 2020-05-26 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0015_auto_20200527_0130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(upload_to='devconnector/images'),
        ),
    ]