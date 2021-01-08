# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename


class OperationalReading(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, default= '')
    badge_number = models.CharField(max_length=100, default= '')
    current_value = models.CharField(max_length=100, default= '')
    measurent_identifier = models.CharField(max_length=100, default= '')
    measurent_type = models.CharField(max_length=100, default= '')
    initial_value_flag = models.CharField(max_length=100, default= '')
    owning_organization = models.CharField(max_length=100, default= '')
    reading_datetime = models.DateTimeField(auto_now=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.asset_id


class WorkRequest(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    description = models.CharField(max_length=100, default= '')
    long_description = models.TextField(max_length=512, default= '')
    required_by_date = models.DateField(auto_now=True)
    approval_profile = models.CharField(max_length=100, default= '')
    bo  = models.CharField(max_length=100, default= '')

    downtime_start = models.DateTimeField(auto_now=True)
    planner  = models.CharField(max_length=100, default= '')
    work_class = models.CharField(max_length=100, default= '')
    work_category = models.CharField(max_length=100, default= '')
    work_priority = models.IntegerField(default=1)
    requestor = models.CharField(max_length=100, default= '')
    owning_access_group = models.CharField(max_length=100, default= '')
    first_name = models.CharField(max_length=100, default= '')
    last_name = models.CharField(max_length=100, default= '')
    primary_phone = models.CharField(max_length=100, default= '')
    mobile_phone = models.CharField(max_length=100, default= '')
    home_phone = models.CharField(max_length=100, default= '')
    node_id = models.CharField(max_length=100, default= '')
    asset_id = models.CharField(max_length=100, default= '')

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, default= '')
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.asset_id

class QuestionsValidValue(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    seq_valid = models.CharField(max_length=100, default= '')
    code_valid = models.CharField(max_length=100, default= '')
    short_text_valid = models.CharField(max_length=100, default= '')
    text_valid = models.CharField(max_length=100, default= '')

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

class ServiceHistoriesQuestions(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    seq = models.CharField(max_length=100, default= '')
    code = models.CharField(max_length=100, default= '')
    short_text = models.CharField(max_length=100, default= '')
    text = models.CharField(max_length=100, default= '')
    style = models.CharField(max_length=100, default= '')
    valid_value = models.ManyToManyField(QuestionsValidValue, null=True)
    respone = models.CharField(max_length=100, default= '')
    response_check_box = models.CharField(max_length=100,default='')
    response_radio = models.CharField(max_length=100,default='')
    responseDate = models.DateField(null=True)
    response_datetime = models.DateTimeField(auto_now=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class AssetLocationAssetListServiceHistories(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    service_history_type = models.CharField(max_length=100,default='')
    effective_datetime = models.DateTimeField(auto_now=True)
    start_date_time = models.DateTimeField(auto_now=True)
    end_date_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=100, default= '')
    failure_type = models.CharField(max_length=100, default= '')
    failure_mode = models.CharField(max_length=100, default= '')
    failure_repair = models.CharField(max_length=100, default= '')
    failure_component = models.CharField(max_length=100, default= '')
    failure_root_cause = models.CharField(max_length=100, default= '')
    question = models.ManyToManyField(ServiceHistoriesQuestions, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

class WorkOrderActivityCompletionAssetLocationAssetList(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    node_id = models.CharField(max_length=100, default= '')
    asset_id = models.CharField(max_length=100, default= '')
    participation = models.CharField(max_length=100, default= '')
    service_histories = models.ManyToManyField(AssetLocationAssetListServiceHistories, null=True)
    measurent_type = models.CharField(max_length=100, default= '')
    reading_type = models.CharField(max_length=100, default= '')
    current_value = models.CharField(max_length=100, default= '')
    reading_datetime = models.DateTimeField(auto_now=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

class WorkOrderActivityCompletion(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    activityid = models.CharField(max_length=100, default= '')
    completiondatetime = models.DateTimeField(auto_now=True)
    asset_location_asset_list = models.ManyToManyField(WorkOrderActivityCompletionAssetLocationAssetList, null=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
