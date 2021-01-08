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
    location_type = models.CharField(max_length=100, default= '')
    locatin_disposition = models.CharField(max_length=100, default= '')
    Bo = models.CharField(max_length=100, default= '')
    description = models.CharField(max_length=100, default= '')
    parent_loc_or_org = models.CharField(max_length=100, default= '')
    work_request_approval_profile = models.CharField(max_length=100, default= '')
    owning_org = models.CharField(max_length=100, default= '')

    building = models.CharField(max_length=100, default= '')
    room = models.CharField(max_length=100, default= '')
    position = models.CharField(max_length=100, default= '')
    country = models.CharField(max_length=100, default= '')
    address_1 = models.CharField(max_length=100, default= '')
    address_2 = models.CharField(max_length=100, default= '')
    address_3 = models.CharField(max_length=100, default= '')
    cross_street = models.CharField(max_length=100, default= '')
    city = models.CharField(max_length=100, default= '')
    suburb = models.CharField(max_length=100, default= '')
    state = models.CharField(max_length=100, default= '')
    postal = models.CharField(max_length=100, default= '')
    location_class = models.CharField(max_length=100, default= '')

    main_contact = models.CharField(max_length=100, default= '')
    maintenance_manager = models.CharField(max_length=100, default= '')
    planner = models.CharField(max_length=100, default= '')
    cost_center = models.CharField(max_length=100, default= '')

    rcm_system = models.CharField(max_length=100, default= '')
    environmental_rating = models.CharField(max_length=100, default= '')
    service_condition = models.CharField(max_length=100, default= '')
    duty_cycle = models.CharField(max_length=100, default= '')
    backlog_group = models.CharField(max_length=100, default= '')
    run_to_failure = models.CharField(max_length=100, default= '')
    breaker = models.CharField(max_length=100, default= '')
    runtime_source = models.CharField(max_length=100, default= '')
    tag_number = models.CharField(max_length=100, default= '')
    site_location = models.CharField(max_length=100, default= '')
    point_id = models.CharField(max_length=100, default= '')
    service_area = models.CharField(max_length=100, default= '')
    latitude = models.CharField(max_length=100, default= '')
    longitude = models.CharField(max_length=100, default= '')
    asset_criticality = models.CharField(max_length=100, default= '')
    criticality_reason = models.CharField(max_length=100, default= '')
    gis_id = models.CharField(max_length=100, default= '')
    connected_to_location_id = models.CharField(max_length=100, default= '')
    water_asset_category = models.CharField(max_length=100, default= '')
    land_asset_status = models.CharField(max_length=100, default= '')
    land_ownership_number = models.CharField(max_length=100, default= '')
    take_over_date = models.DateField(null=True)
    take_over_date_source_qt11 = models.DateField(null=True)
    take_over_date_source_ccc = models.DateField(null=True)
    land_area_acre = models.CharField(max_length=100, default= '')
    plan_certified_number = models.CharField(max_length=100, default= '')
    plan_pre_computation_number = models.CharField(max_length=100, default= '')
    plan_as_built_number = models.CharField(max_length=100, default= '')
    quit_rent_bill_number = models.CharField(max_length=100, default= '')
    current_rate_of_quit_rent = models.CharField(max_length=100, default= '')
    quit_rent_bill_payment_date = models.DateField(null=True)
    assessment_bill_number = models.CharField(max_length=100, default= '')
    current_rate_of_assesment = models.CharField(max_length=100, default= '')
    assessment_bill_payment_date = models.CharField(max_length=100, default= '')
    lease_expired_date = models.DateField(null=True)
    remarks = models.CharField(max_length=100, default= '' )

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.work_request_approval_profile

class AssetMeasurementType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measurement_type = models.CharField(max_length=100, default= '' )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.measurement_type


class AssetAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic_type = models.CharField(max_length=100, default= '' )
    adhoc_value = models.CharField(max_length=100, default= '' )
    characteristic_value = models.CharField(max_length=100, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.characteristic_type + ' ' + self.adhoc_value + ' ' + self.characteristic_value


class Asset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, default= '' )
    asset_type = models.CharField(max_length=100, default= '' )
    transaction_type = models.CharField(max_length=100, default= '' )
    description = models.CharField(max_length=100, default= '')
    bo = models.CharField(max_length=100, default= '')
    bo_status = models.CharField(max_length=100, default= '')
    owning_access_group = models.CharField(max_length=100, null=True, blank=True)
    effective_datetime = models.DateTimeField(auto_now=True)
    node_id = models.CharField(max_length=100, default= '')
    badge_no = models.CharField(max_length=100, default= '')
    serial_no = models.CharField(max_length=100, default= '')
    pallet_no = models.CharField(max_length=100, default= '')
    handed_over_asset = models.CharField(max_length=100, default= '')
    fixed_asset_no = models.CharField(max_length=100, default= '')
    scada_id = models.CharField(max_length=100, default= '')
    condition_rating = models.CharField(max_length=100, default= '')
    condifence_rating = models.CharField(max_length=100, default= '')
    maintenance_specification = models.CharField(max_length=100, default= '')
    measurement_types = models.ManyToManyField(AssetMeasurementType, null=True)
    bom_part_id = models.CharField(max_length=100, default= '')
    attached_to_asset_id = models.CharField(max_length=100, default= '')
    vehicle_identification_num = models.CharField(max_length=100, default= '')
    license_number = models.CharField(max_length=100, default= '')
    purchase_order_num = models.CharField(max_length=100, default= '')
    location_id = models.CharField(max_length=100, default= '')
    metrology_firmware = models.CharField(max_length=100, default= '')
    nic_firmware = models.CharField(max_length=100, default= '')
    configuration = models.CharField(max_length=100, default= '')
    warranty_expiration_date = models.DateField(null=True)
    warranty_detail = models.CharField(max_length=100, default= '')
    vendor_part_no = models.CharField(max_length=100, default= '')
    asset_attributes = models.ManyToManyField(AssetAttribute, null=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.asset_id
