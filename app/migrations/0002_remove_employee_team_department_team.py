# Generated by Django 4.1.1 on 2022-10-12 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='team',
        ),
        migrations.AddField(
            model_name='department',
            name='team',
            field=models.TextField(default=''),
        ),
    ]
