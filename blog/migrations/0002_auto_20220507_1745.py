# Generated by Django 3.2 on 2022-05-07 17:45

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image',
        ),
        migrations.AddField(
            model_name='post',
            name='post_image',
            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('R', 'Reviews'), ('A', 'Announcements'), ('N', 'News'), ('O', 'Opinion'), ('P', 'Previews'), ('S', 'Streaming'), ('T', 'Tech'), ('M', 'Miscellaneous')], max_length=4),
        ),
    ]
