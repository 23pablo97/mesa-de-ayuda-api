# Generated by Django 3.0.5 on 2020-10-05 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('process', '0007_delete_steps'),
    ]

    operations = [
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('published', models.BooleanField(default=True)),
                ('process', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='process.Process')),
            ],
        ),
        migrations.CreateModel(
            name='Steps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('name', models.CharField(default='', max_length=200)),
                ('description', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('instance', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='instances.Instance')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('instance', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='instances.Instance')),
            ],
        ),
    ]