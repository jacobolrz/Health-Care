# Generated by Django 4.1.1 on 2022-10-16 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0009_rename_user_type_profile_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='profile',
        ),
        migrations.AddField(
            model_name='profile',
            name='user_type',
            field=models.CharField(default='1', max_length=50, null=True),
        ),
    ]
