# Generated by Django 4.1.1 on 2022-10-16 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cr', '0004_alter_profile_user_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('medical_speciality', models.CharField(max_length=50)),
                ('license', models.CharField(max_length=50)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='birthday_year',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='doctor',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='Ailments',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='Allergies',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user_type',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Patient', 'Patient')], max_length=20),
        ),
        migrations.DeleteModel(
            name='Costumer',
        ),
    ]
