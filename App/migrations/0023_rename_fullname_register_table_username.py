# Generated by Django 4.2.6 on 2023-10-13 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0022_remove_login_table_fullname_register_table_fullname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register_table',
            old_name='fullname',
            new_name='username',
        ),
    ]