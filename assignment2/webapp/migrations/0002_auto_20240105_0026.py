# Generated by Django 3.0.2 on 2024-01-04 18:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='emp',
            old_name='Salary',
            new_name='Age',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='Position',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='emp',
            old_name='Eid',
            new_name='ID',
        ),
    ]
