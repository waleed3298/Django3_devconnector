# Generated by Django 3.0.5 on 2020-05-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0010_auto_20200526_0124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(null=True, upload_to='devconnector/images'),
        ),
    ]
