# Generated by Django 4.1.3 on 2022-11-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_description_remove_user_github link_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='logo',
            field=models.ImageField(blank=True, upload_to='media', verbose_name='Logo'),
        ),
    ]
