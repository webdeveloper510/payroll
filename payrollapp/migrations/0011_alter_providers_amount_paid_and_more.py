# Generated by Django 4.1.3 on 2023-01-12 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0010_alter_providers_amount_paid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='providers',
            name='amount_paid',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='providers',
            name='days_overdue',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
