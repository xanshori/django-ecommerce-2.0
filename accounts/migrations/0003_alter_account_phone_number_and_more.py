# Generated by Django 4.1.3 on 2023-01-04 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]