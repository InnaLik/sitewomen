# Generated by Django 4.2.5 on 2024-03-14 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0028_country_alter_day_options_alter_holiday_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='holiday',
            name='country',
            field=models.ManyToManyField(blank=True, to='main_page.country'),
        ),
    ]
