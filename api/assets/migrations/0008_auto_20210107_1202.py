# Generated by Django 2.2 on 2021-01-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20201221_1136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assetlocation',
            name='Assessment_Bill_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Assessment_Bill_Payment_Date',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Bo',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Connected_to_Location_ID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Current_Rate_Of_Assesment',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Current_Rate_of_Quit_Rent',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='GisID',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Land_Area_Acre',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Land_Asset_Status',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Land_Ownership_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Plan_As_Built_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Plan_Certified_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Plan_Pre_Computation_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Quit_Rent_Bill_Number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Remarks',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Water_Asset_Category',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='address_1',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='address_2',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='address_3',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='asset_criticality',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='backlog_group',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='breaker',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='building',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='cost_center',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='criticality_reason',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='cross_street',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='description',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='duty_cycle',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='environmental_rating',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='latitude',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='locatin_disposition',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='location_class',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='location_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='longitude',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='main_contact',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='maintenance_manager',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='owning_org',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='parent_loc_or_org',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='planner',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='point_id',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='postal',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='rcm_system',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='room',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='run_to_failure',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='runtime_source',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='service_area',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='service_condition',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='site_location',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='suburb',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='tag_number',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='work_request_approval_profile',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
