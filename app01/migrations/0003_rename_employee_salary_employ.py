# Generated by Django 4.1.3 on 2022-12-02 07:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_employee_salary'),
    ]

    operations = [
        migrations.RenameField(
            model_name='salary',
            old_name='employee',
            new_name='employ',
        ),
    ]
