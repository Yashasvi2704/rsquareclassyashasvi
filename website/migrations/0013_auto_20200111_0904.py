# Generated by Django 3.0.2 on 2020-01-11 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_rsquareuser_phone_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rsquareuser',
            old_name='phone_number',
            new_name='phone_no',
        ),
    ]
