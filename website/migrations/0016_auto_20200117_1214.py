# Generated by Django 3.0.2 on 2020-01-17 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0015_academicyear_batch'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='subject',
        ),
        migrations.CreateModel(
            name='BatchSubjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_1', to='website.Batch')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related', to='website.Subject')),
            ],
        ),
    ]
