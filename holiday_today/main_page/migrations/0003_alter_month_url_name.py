# Generated by Django 4.2.5 on 2024-01-30 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0002_month_url_name_alter_month_name_month_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='month',
            name='url_name',
            field=models.SlugField(unique=True),
        ),
    ]
