# Generated by Django 4.2.5 on 2024-03-10 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0025_day_month'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='holiday',
            name='day',
        ),
        migrations.RemoveField(
            model_name='holiday',
            name='month',
        ),
    ]
