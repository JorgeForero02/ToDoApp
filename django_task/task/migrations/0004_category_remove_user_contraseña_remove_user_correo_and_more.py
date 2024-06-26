# Generated by Django 5.0.4 on 2024-04-30 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_remove_task_prioridad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='contraseña',
        ),
        migrations.RemoveField(
            model_name='user',
            name='correo',
        ),
        migrations.RemoveField(
            model_name='user',
            name='nombre',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='user_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
