# Generated by Django 2.0.8 on 2018-11-24 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cyblog', '0004_auto_20181124_1635'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_infos',
            old_name='username',
            new_name='user',
        ),
    ]
