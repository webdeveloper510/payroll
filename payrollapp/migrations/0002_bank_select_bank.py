# Generated by Django 4.1.3 on 2023-01-02 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payrollapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank',
            name='select_bank',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]