# Generated by Django 4.1.1 on 2022-10-16 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0005_doctors_remove_patient_birthday_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(max_length=50),
        ),
    ]