# Generated by Django 3.1.1 on 2022-08-04 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cheese',
            name='name',
        ),
    ]
