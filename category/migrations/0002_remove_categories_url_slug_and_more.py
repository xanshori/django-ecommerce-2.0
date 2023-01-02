# Generated by Django 4.1.3 on 2022-12-31 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categories',
            name='url_slug',
        ),
        migrations.RemoveField(
            model_name='subcategories',
            name='url_slug',
        ),
        migrations.AddField(
            model_name='categories',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subcategories',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
