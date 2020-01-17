# Generated by Django 3.0.2 on 2020-01-08 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_branch'),
    ]

    operations = [
        migrations.AddField(
            model_name='rsquareuser',
            name='role',
            field=models.CharField(choices=[('OWNER', 'Owner'), ('BRANCHMANAGER', 'Branch Manager'), ('ACCOUNTANT', 'Accountant'), ('TEACHER', 'Teacher'), ('STUDENT', 'Student')], default='OWNER', max_length=20),
        ),
    ]