# Generated by Django 4.1.3 on 2023-01-02 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0003_remove_bank_select_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='providers',
            name='bank_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='providers',
            name='bank_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]