# Generated by Django 4.2.5 on 2024-04-14 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('women', '0012_uploadfiles_alter_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='women',
            name='photo',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='photos/%Y/%m/%d', verbose_name='Фото'),
        ),
    ]
