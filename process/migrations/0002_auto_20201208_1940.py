# Generated by Django 3.0.5 on 2020-12-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='process',
            name='banner_description',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='process',
            name='icon',
            field=models.TextField(default=''),
        ),
    ]
