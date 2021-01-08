# Generated by Django 2.2 on 2021-01-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_auto_20201218_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='comments',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='failure_component',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='failure_mode',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='failure_repair',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='failure_root_cause',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='failure_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocationassetlistservicehistories',
            name='service_history_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='asset_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='badge_number',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='current_value',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='initial_value_flag',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='measurent_identifier',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='measurent_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='operationalreading',
            name='owning_organization',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionsvalidvalue',
            name='code_valid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionsvalidvalue',
            name='seq_valid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionsvalidvalue',
            name='short_text_valid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='questionsvalidvalue',
            name='text_valid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='code',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='respone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='response_check_box',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='response_radio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='seq',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='short_text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='style',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='servicehistoriesquestions',
            name='text',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletion',
            name='activityid',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletionassetlocationassetlist',
            name='asset_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletionassetlocationassetlist',
            name='current_value',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletionassetlocationassetlist',
            name='measurent_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletionassetlocationassetlist',
            name='node_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletionassetlocationassetlist',
            name='participation',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workorderactivitycompletionassetlocationassetlist',
            name='reading_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='approval_profile',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='asset_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='bo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='created_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='description',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='first_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='home_phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='long_description',
            field=models.TextField(max_length=512),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='mobile_phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='node_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='owning_access_group',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='planner',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='primary_phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='requestor',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='work_category',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='workrequest',
            name='work_class',
            field=models.CharField(max_length=100),
        ),
    ]
