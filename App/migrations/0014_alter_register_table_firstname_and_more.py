# Generated by Django 4.2.5 on 2023-10-05 07:20

import App.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_alter_register_table_firstname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='firstname',
            field=models.CharField(max_length=200, validators=[App.models.validate_password_model, django.core.validators.RegexValidator('^[a-zA-Z]*$', message='Only alphabets are allowed')]),
        ),
        migrations.AlterField(
            model_name='register_table',
            name='lastname',
            field=models.CharField(max_length=200, validators=[App.models.validate_password_model, django.core.validators.RegexValidator('^[a-zA-Z]*$', message='Only alphabets are allowed')]),
        ),
    ]