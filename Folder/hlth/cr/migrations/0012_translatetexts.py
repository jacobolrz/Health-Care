# Generated by Django 4.1 on 2022-10-17 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cr', '0011_costumer_remove_doctor_phone_number_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TranslateTexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('language_code_origin', models.CharField(choices=[('en', 'english'), ('fr', 'french'), ('de', 'deutch'), ('it', 'italian'), ('es', 'spanish')], max_length=2)),
                ('language_code_destiny', models.CharField(choices=[('en', 'english'), ('fr', 'french'), ('de', 'deutch'), ('it', 'italian'), ('es', 'spanish')], max_length=2)),
                ('text_to_translate', models.CharField(max_length=255)),
                ('text_translated', models.CharField(max_length=255)),
            ],
        ),
    ]
