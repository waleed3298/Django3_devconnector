# Generated by Django 3.0.5 on 2020-06-14 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0034_posts_dislikes'),
    ]

    operations = [
        migrations.AddField(
            model_name='posts',
            name='liked',
            field=models.BooleanField(default=False),
        ),
    ]