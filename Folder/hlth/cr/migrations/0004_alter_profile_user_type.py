# Generated by Django 4.1.1 on 2022-10-16 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0003_remove_doctor_phone_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(max_length=20),
        ),
    ]
