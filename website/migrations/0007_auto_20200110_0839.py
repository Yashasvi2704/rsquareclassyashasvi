# Generated by Django 3.0.2 on 2020-01-10 03:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200110_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursesubject',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel', to='website.Course'),
        ),
        migrations.AlterField(
            model_name='coursesubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rel', to='website.Subject'),
        ),
    ]