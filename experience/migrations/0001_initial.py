# Generated by Django 4.1.3 on 2022-12-11 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('period', models.CharField(default='2018 - 2019', help_text='The period of the current experience.', max_length=40, verbose_name='Period')),
                ('description', models.TextField(default='My job is to build your website...', help_text='A little description of this experience.', verbose_name='Description')),
                ('type', models.CharField(choices=[('ex', 'Experience'), ('ed', 'Education')], default='ex', max_length=12, verbose_name='Type')),
                ('position', models.IntegerField(default=1, help_text='Choose the position depending to the type in the view.', verbose_name='Position')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]