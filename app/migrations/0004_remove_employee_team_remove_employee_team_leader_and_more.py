# Generated by Django 4.1.1 on 2022-10-11 22:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_team_leader_employee_team_leader_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='team',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='team_Leader',
        ),
        migrations.AlterField(
            model_name='employee',
            name='hourly_Rate',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='weekly_Work_Hour',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='work',
            field=models.TextField(default=''),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team', models.TextField(default='')),
                ('team_Leader', models.TextField(default='')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.employee')),
            ],
        ),
    ]