# Generated by Django 4.1.3 on 2022-12-12 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0002_user_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider_name', models.CharField(blank=True, max_length=250, null=True)),
                ('invoice', models.CharField(blank=True, max_length=250, null=True)),
                ('issue_date', models.DateField(blank=True)),
                ('total_amount_paid', models.CharField(blank=True, max_length=250, null=True)),
                ('amount_paid', models.CharField(blank=True, max_length=250, null=True)),
                ('balance_payable', models.CharField(blank=True, max_length=250, null=True)),
                ('payment_policy', models.CharField(blank=True, max_length=250, null=True)),
                ('expiration_date', models.DateField(blank=True)),
                ('payment_week', models.CharField(blank=True, max_length=250, null=True)),
                ('month_of_payment', models.CharField(blank=True, max_length=250, null=True)),
                ('year_of_payment', models.CharField(blank=True, max_length=250, null=True)),
                ('range_to_pay', models.CharField(blank=True, max_length=250, null=True)),
                ('days_overdue', models.CharField(blank=True, max_length=250, null=True)),
                ('overdue', models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]
