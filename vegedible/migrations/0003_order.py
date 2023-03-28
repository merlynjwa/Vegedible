# Generated by Django 3.2.18 on 2023-03-28 02:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vegedible', '0002_rename_customers_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_and_time', models.DateTimeField()),
                ('table_number', models.IntegerField(unique_for_date=models.DateTimeField(), validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)])),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegedible.customer')),
            ],
        ),
    ]