# Generated by Django 5.0.4 on 2024-04-24 23:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='prioridad',
        ),
    ]
