# Generated by Django 4.2.5 on 2024-01-30 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0004_day'),
    ]

    operations = [
        migrations.CreateModel(
            name='Holiday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url_name', models.SlugField(unique=True)),
                ('international', models.BooleanField(default=False)),
                ('worldwide', models.BooleanField(default=False)),
                ('ordinary_holiday', models.BooleanField(default=False)),
            ],
        ),
    ]
