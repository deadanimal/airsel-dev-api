# Generated by Django 2.2 on 2021-01-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0012_auto_20210108_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='operationalreading',
            name='submitted_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workorderactivitycompletion',
            name='submitted_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='workrequest',
            name='submitted_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
