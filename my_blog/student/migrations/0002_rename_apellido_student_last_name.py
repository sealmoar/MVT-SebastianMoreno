# Generated by Django 4.1.2 on 2022-10-12 04:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='apellido',
            new_name='last_name',
        ),
    ]