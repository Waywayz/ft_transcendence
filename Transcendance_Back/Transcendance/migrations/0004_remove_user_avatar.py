# Generated by Django 4.2.10 on 2024-03-07 00:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Transcendance', '0003_alter_user_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
