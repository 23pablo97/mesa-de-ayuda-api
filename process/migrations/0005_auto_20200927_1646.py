# Generated by Django 3.0.5 on 2020-09-27 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0004_auto_20200927_0845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='steps',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
