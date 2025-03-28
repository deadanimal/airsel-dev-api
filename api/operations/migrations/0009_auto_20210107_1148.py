# Generated by Django 2.2 on 2021-01-07 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0008_auto_20210108_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operationalreading',
            name='asset_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='badge_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='current_value',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='initial_value_flag',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='measurent_identifier',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='measurent_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='owning_organization',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
