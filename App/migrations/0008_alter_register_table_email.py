# Generated by Django 4.2.5 on 2023-10-02 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_alter_register_table_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register_table',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
