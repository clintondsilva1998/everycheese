# Generated by Django 3.1.1 on 2022-08-04 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cheeses', '0003_cheese_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cheese',
            old_name='frimness',
            new_name='firmness',
        ),
    ]