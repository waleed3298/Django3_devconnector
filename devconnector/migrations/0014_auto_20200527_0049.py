# Generated by Django 3.0.5 on 2020-05-26 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('devconnector', '0013_auto_20200526_1918'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='post',
        ),
        migrations.AddField(
            model_name='comments',
            name='p_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='devconnector.Posts'),
        ),
    ]
