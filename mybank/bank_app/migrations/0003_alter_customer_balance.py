# Generated by Django 4.1.6 on 2023-02-08 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_app', '0002_contact_us_alter_transaction_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Balance',
            field=models.CharField(max_length=10),
        ),
    ]
