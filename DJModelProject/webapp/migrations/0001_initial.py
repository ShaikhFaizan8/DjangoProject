# Generated by Django 3.0.2 on 2023-12-22 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empid', models.IntegerField()),
                ('empname', models.CharField(max_length=30)),
                ('empsal', models.IntegerField()),
                ('empadd', models.CharField(max_length=30)),
            ],
        ),
    ]
