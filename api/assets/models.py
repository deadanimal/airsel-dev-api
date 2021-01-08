# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename


# class AssetLocationCostCenter(models.Model):
#
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     cost_center = models.CharField(max_length=100, default='NA')
#     percentage = models.FloatField(default=0)
#
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#
#     class meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.cost_center

# class AssetLocationCriticalityReason(models.Model):
#
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     criticality_reason = models.CharField(max_length=100, default='NA')
#
#     created_date = models.DateTimeField(auto_now_add=True)
#     modified_date = models.DateTimeField(auto_now=True)
#
#     class meta:
#         ordering = ['-created_date']
#
#     def __str__(self):
#         return self.criticality_reason

class AssetLocation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location_type = models.CharField(max_length=100, blank=True)
    locatin_disposition = models.CharField(max_length=100, blank=True)
    Bo = models.CharField(max_length=100, blank=True)
    description = models.CharField(max_length=100, blank=True)
    parent_loc_or_org = models.CharField(max_length=100, blank=True)
    work_request_approval_profile = models.CharField(max_length=100, blank=True)
    owning_org = models.CharField(max_length=100, blank=True)

    building = models.CharField(max_length=100, blank=True)
    room = models.CharField(max_length=100, blank=True)
    position = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    address_1 = models.CharField(max_length=100, blank=True)
    address_2 = models.CharField(max_length=100, blank=True)
    address_3 = models.CharField(max_length=100, blank=True)
    cross_street = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    suburb = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    postal = models.CharField(max_length=100, blank=True)
    location_class = models.CharField(max_length=100, blank=True)

    main_contact = models.CharField(max_length=100, blank=True)
    maintenance_manager = models.CharField(max_length=100, blank=True)
    planner = models.CharField(max_length=100, blank=True)
    cost_center = models.CharField(max_length=100, blank=True)

    rcm_system = models.CharField(max_length=100, blank=True)
    environmental_rating = models.CharField(max_length=100, blank=True)
    service_condition = models.CharField(max_length=100, blank=True)
    duty_cycle = models.CharField(max_length=100, blank=True)
    backlog_group = models.CharField(max_length=100, blank=True)
    run_to_failure = models.CharField(max_length=100, blank=True)
    breaker = models.CharField(max_length=100, blank=True)
    runtime_source = models.CharField(max_length=100, blank=True)
    tag_number = models.CharField(max_length=100, blank=True)
    site_location = models.CharField(max_length=100, blank=True)
    point_id = models.CharField(max_length=100, blank=True)
    service_area = models.CharField(max_length=100, blank=True)
    latitude = models.CharField(max_length=100, blank=True)
    longitude = models.CharField(max_length=100, blank=True)
    asset_criticality = models.CharField(max_length=100, blank=True)
    criticality_reason = models.CharField(max_length=100, blank=True)
    GisID = models.CharField(max_length=100, blank=True)
    Connected_to_Location_ID = models.CharField(max_length=100, blank=True)
    Water_Asset_Category = models.CharField(max_length=100, blank=True)
    Land_Asset_Status = models.CharField(max_length=100, blank=True)
    Land_Ownership_Number = models.CharField(max_length=100, blank=True)
    Take_Over_Date = models.DateField(null=True)
    Take_Over_Date_Source_QT11 = models.DateField(null=True)
    Take_Over_Date_Source_CCC = models.DateField(null=True)
    Land_Area_Acre = models.CharField(max_length=100, blank=True)
    Plan_Certified_Number = models.CharField(max_length=100, blank=True)
    Plan_Pre_Computation_Number = models.CharField(max_length=100, blank=True)
    Plan_As_Built_Number = models.CharField(max_length=100, blank=True)
    Quit_Rent_Bill_Number = models.CharField(max_length=100, blank=True)
    Current_Rate_of_Quit_Rent = models.CharField(max_length=100, blank=True)
    Quit_Rent_Bill_Payment_Date = models.DateField(null=True)
    Assessment_Bill_Number = models.CharField(max_length=100, blank=True)
    Current_Rate_Of_Assesment = models.CharField(max_length=100, blank=True)
    Assessment_Bill_Payment_Date = models.CharField(max_length=100, blank=True)
    Lease_Expired_Date = models.DateField(null=True)
    Remarks = models.CharField(max_length=100, blank=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.work_request_approval_profile

class AssetMeasurementType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measurement_type = models.CharField(max_length=100, default='NA')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.measurement_type


class AssetAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic_type = models.CharField(max_length=100, default='NA')
    adhoc_value = models.CharField(max_length=100, default='NA')
    characteristic_value = models.CharField(max_length=100, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.characteristic_type + ' ' + self.adhoc_value + ' ' + self.characteristic_value


class Asset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, default='NA')
    asset_type = models.CharField(max_length=100, default='NA')
    transaction_type = models.CharField(max_length=100, default='NA')
    description = models.CharField(max_length=100, default='NA')
    bo = models.CharField(max_length=100, default='NA')
    bo_status = models.CharField(max_length=100, default='NA')
    owning_access_group = models.CharField(max_length=100, null=True, blank=True)
    effective_datetime = models.DateTimeField(auto_now=True)
    node_id = models.CharField(max_length=100, default='NA')
    badge_no = models.CharField(max_length=100, default='NA')
    serial_no = models.CharField(max_length=100, default='NA')
    pallet_no = models.CharField(max_length=100, default='NA')
    handed_over_asset = models.CharField(max_length=100, default='NA')
    fixed_asset_no = models.CharField(max_length=100, default='NA')
    scada_id = models.CharField(max_length=100, default='NA')
    condition_rating = models.CharField(max_length=100, default='NA')
    condifence_rating = models.CharField(max_length=100, default='NA')
    maintenance_specification = models.CharField(max_length=100, default='NA')
    measurement_types = models.ManyToManyField(AssetMeasurementType, null=True)
    bom_part_id = models.CharField(max_length=100, default='NA')
    attached_to_asset_id = models.CharField(max_length=100, default='NA')
    vehicle_identification_num = models.CharField(max_length=100, default='NA')
    license_number = models.CharField(max_length=100, default='NA')
    purchase_order_num = models.CharField(max_length=100, default='NA')
    location_id = models.CharField(max_length=100, default='NA')
    metrology_firmware = models.CharField(max_length=100, default='NA')
    nic_firmware = models.CharField(max_length=100, default='NA')
    configuration = models.CharField(max_length=100, default='NA')
    warranty_expiration_date = models.DateField(null=True)
    warranty_detail = models.CharField(max_length=100, default='NA')
    vendor_part_no = models.CharField(max_length=100, default='NA')
    asset_attributes = models.ManyToManyField(AssetAttribute, null=True)

    submitted_datetime = models.DateTimeField(null=True, default=None)
    registered_datetime = models.DateTimeField(null=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.asset_id
