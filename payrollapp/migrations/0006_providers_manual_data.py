# Generated by Django 4.1.3 on 2023-01-05 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0005_user_enddate_user_siipassword_user_siiusername_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='manual_data',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
