# Generated by Django 4.1.3 on 2023-01-15 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('experience', '0003_experience_description_en_experience_description_es_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experience',
            name='description_es',
        ),
        migrations.RemoveField(
            model_name='experience',
            name='name_es',
        ),
    ]
