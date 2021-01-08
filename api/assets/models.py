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
    gis_id = models.CharField(max_length=100, blank=True)
    connected_to_location_id = models.CharField(max_length=100, blank=True)
    water_asset_category = models.CharField(max_length=100, blank=True)
    land_asset_status = models.CharField(max_length=100, blank=True)
    land_ownership_number = models.CharField(max_length=100, blank=True)
    take_over_date = models.DateField(null=True)
    take_over_date_source_qt11 = models.DateField(null=True)
    take_over_date_source_ccc = models.DateField(null=True)
    land_area_acre = models.CharField(max_length=100, blank=True)
    plan_certified_number = models.CharField(max_length=100, blank=True)
    plan_pre_computation_number = models.CharField(max_length=100, blank=True)
    plan_as_built_number = models.CharField(max_length=100, blank=True)
    quit_rent_bill_number = models.CharField(max_length=100, blank=True)
    current_rate_of_quit_rent = models.CharField(max_length=100, blank=True)
    quit_rent_bill_payment_date = models.DateField(null=True)
    assessment_bill_number = models.CharField(max_length=100, blank=True)
    current_rate_Of_assesment = models.CharField(max_length=100, blank=True)
    assessment_bill_payment_date = models.CharField(max_length=100, blank=True)
    lease_expired_date = models.DateField(null=True)
    remarks = models.CharField(max_length=100, blank=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.work_request_approval_profile

class AssetMeasurementType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    measurement_type = models.CharField(max_length=100, blank=True )

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.measurement_type


class AssetAttribute(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    characteristic_type = models.CharField(max_length=100, blank=True )
    adhoc_value = models.CharField(max_length=100, blank=True )
    characteristic_value = models.CharField(max_length=100, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.characteristic_type + ' ' + self.adhoc_value + ' ' + self.characteristic_value


class Asset(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, blank=True )
    asset_type = models.CharField(max_length=100, blank=True )
    transaction_type = models.CharField(max_length=100, blank=True )
    description = models.CharField(max_length=100, blank=True)
    bo = models.CharField(max_length=100, blank=True)
    bo_status = models.CharField(max_length=100, blank=True)
    owning_access_group = models.CharField(max_length=100, null=True, blank=True)
    effective_datetime = models.DateTimeField(auto_now=True)
    node_id = models.CharField(max_length=100, blank=True)
    badge_no = models.CharField(max_length=100, blank=True)
    serial_no = models.CharField(max_length=100, blank=True)
    pallet_no = models.CharField(max_length=100, blank=True)
    handed_over_asset = models.CharField(max_length=100, blank=True)
    fixed_asset_no = models.CharField(max_length=100, blank=True)
    scada_id = models.CharField(max_length=100, blank=True)
    condition_rating = models.CharField(max_length=100, blank=True)
    condifence_rating = models.CharField(max_length=100, blank=True)
    maintenance_specification = models.CharField(max_length=100, blank=True)
    measurement_types = models.ManyToManyField(AssetMeasurementType, null=True)
    bom_part_id = models.CharField(max_length=100, blank=True)
    attached_to_asset_id = models.CharField(max_length=100, blank=True)
    vehicle_identification_num = models.CharField(max_length=100, blank=True)
    license_number = models.CharField(max_length=100, blank=True)
    purchase_order_num = models.CharField(max_length=100, blank=True)
    location_id = models.CharField(max_length=100, blank=True)
    metrology_firmware = models.CharField(max_length=100, blank=True)
    nic_firmware = models.CharField(max_length=100, blank=True)
    configuration = models.CharField(max_length=100, blank=True)
    warranty_expiration_date = models.DateField(null=True)
    warranty_detail = models.CharField(max_length=100, blank=True)
    vendor_part_no = models.CharField(max_length=100, blank=True)
    asset_attributes = models.ManyToManyField(AssetAttribute, null=True)

    submitted_datetime = models.DateTimeField(null=True, default=None)
    registered_datetime = models.DateTimeField(null=True, default=None)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.asset_id
