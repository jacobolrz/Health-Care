# Generated by Django 4.1.1 on 2022-10-16 04:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0008_alter_doctor_license'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user_type',
            new_name='profile',
        ),
    ]
