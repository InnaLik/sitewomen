# Generated by Django 4.2.5 on 2024-04-15 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0031_alter_holiday_month'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileUploadHoliday',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='image')),
            ],
        ),
    ]
