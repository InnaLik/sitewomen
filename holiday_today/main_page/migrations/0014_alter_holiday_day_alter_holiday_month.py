# Generated by Django 4.2.5 on 2024-02-08 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0013_rename_date_id_holiday_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='holiday',
            name='day',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_page.day'),
        ),
        migrations.AlterField(
            model_name='holiday',
            name='month',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='main_page.month'),
        ),
    ]
