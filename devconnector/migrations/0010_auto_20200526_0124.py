# Generated by Django 3.0.5 on 2020-05-25 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0009_auto_20200525_1648'),
    ]

    operations = [
        migrations.AddField(
            model_name='developer',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='developer',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
