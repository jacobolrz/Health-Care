# Generated by Django 4.1.1 on 2022-10-16 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cr', '0010_remove_profile_profile_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=20)),
                ('location', models.CharField(max_length=100)),
                ('medical_speciality', models.CharField(max_length=50)),
                ('license', models.CharField(max_length=50)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='Ailments',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='birthday_year',
            field=models.CharField(default=2, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='doctor',
            name='license',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Allergies',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Doctors',
        ),
    ]
