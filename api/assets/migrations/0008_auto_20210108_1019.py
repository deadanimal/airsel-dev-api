# Generated by Django 2.2 on 2021-01-08 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assets', '0007_auto_20201221_1136'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assetlocation',
            old_name='Lease_Expired_Date',
            new_name='lease_expired_date',
        ),
        migrations.RenameField(
            model_name='assetlocation',
            old_name='Quit_Rent_Bill_Payment_Date',
            new_name='quit_rent_bill_payment_date',
        ),
        migrations.RenameField(
            model_name='assetlocation',
            old_name='Take_Over_Date',
            new_name='take_over_date',
        ),
        migrations.RenameField(
            model_name='assetlocation',
            old_name='Take_Over_Date_Source_CCC',
            new_name='take_over_date_source_ccc',
        ),
        migrations.RenameField(
            model_name='assetlocation',
            old_name='Take_Over_Date_Source_QT11',
            new_name='take_over_date_source_qt11',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Assessment_Bill_Number',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Assessment_Bill_Payment_Date',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Connected_to_Location_ID',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Current_Rate_Of_Assesment',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Current_Rate_of_Quit_Rent',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='GisID',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Land_Area_Acre',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Land_Asset_Status',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Land_Ownership_Number',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Plan_As_Built_Number',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Plan_Certified_Number',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Plan_Pre_Computation_Number',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Quit_Rent_Bill_Number',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Remarks',
        ),
        migrations.RemoveField(
            model_name='assetlocation',
            name='Water_Asset_Category',
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='assessment_bill_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='assessment_bill_payment_date',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='connected_to_location_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='current_rate_of_assesment',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='current_rate_of_quit_rent',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='gis_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='land_area_acre',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='land_asset_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='land_ownership_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='plan_as_built_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='plan_certified_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='plan_pre_computation_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='quit_rent_bill_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='remarks',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='assetlocation',
            name='water_asset_category',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='asset_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='attached_to_asset_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='badge_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='bo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='bo_status',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='bom_part_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='condifence_rating',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='condition_rating',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='configuration',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='fixed_asset_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='handed_over_asset',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='license_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='location_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='maintenance_specification',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='metrology_firmware',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='nic_firmware',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='node_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='pallet_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='purchase_order_num',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='scada_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='serial_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='transaction_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='vehicle_identification_num',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='vendor_part_no',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='asset',
            name='warranty_detail',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetattribute',
            name='adhoc_value',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetattribute',
            name='characteristic_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='Bo',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='address_1',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='address_2',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='address_3',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='asset_criticality',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='backlog_group',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='breaker',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='building',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='cost_center',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='country',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='criticality_reason',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='cross_street',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='description',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='duty_cycle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='environmental_rating',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='latitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='locatin_disposition',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='location_class',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='location_type',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='longitude',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='main_contact',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='maintenance_manager',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='owning_org',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='parent_loc_or_org',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='planner',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='point_id',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='position',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='postal',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='rcm_system',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='room',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='run_to_failure',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='runtime_source',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='service_area',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='service_condition',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='site_location',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='state',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='suburb',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='tag_number',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetlocation',
            name='work_request_approval_profile',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='assetmeasurementtype',
            name='measurement_type',
            field=models.CharField(default='', max_length=100),
        ),
    ]
