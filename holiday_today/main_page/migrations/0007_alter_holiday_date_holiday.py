# Generated by Django 4.2.5 on 2024-01-31 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_holiday_date_holiday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='date_holiday',
            field=models.CharField(max_length=255),
        ),
    ]
