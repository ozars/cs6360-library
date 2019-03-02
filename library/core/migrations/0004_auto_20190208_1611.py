# Generated by Django 2.2a1 on 2019-02-08 22:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_borrower_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='ISBN must consist of ten digits.', regex='^\\d{10}$')], verbose_name='ISBN'),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='bname',
            field=models.CharField(max_length=64, verbose_name='Borrower'),
        ),
        migrations.AlterField(
            model_name='borrower',
            name='ssn',
            field=models.CharField(max_length=9, unique=True, verbose_name='SSN'),
        ),
    ]
