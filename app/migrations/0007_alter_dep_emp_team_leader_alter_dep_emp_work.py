# Generated by Django 4.1.1 on 2022-10-12 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_dep_emp_team'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dep_emp',
            name='team_Leader',
            field=models.TextField(choices=[('TRUE', 'YES'), ('FALSE', 'NO')], default=''),
        ),
        migrations.AlterField(
            model_name='dep_emp',
            name='work',
            field=models.TextField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time')], default=''),
        ),
    ]
