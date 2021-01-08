# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import uuid

from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from simple_history.models import HistoricalRecords

from core.helpers import PathAndRename


class OperationalReading(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    asset_id = models.CharField(max_length=100, blank=True)
    badge_number = models.CharField(max_length=100, blank=True)
    current_value = models.CharField(max_length=100, blank=True)
    measurent_identifier = models.CharField(max_length=100, blank=True)
    measurent_type = models.CharField(max_length=100, blank=True)
    initial_value_flag = models.CharField(max_length=100, blank=True)
    owning_organization = models.CharField(max_length=100, blank=True)
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
    description = models.CharField(max_length=100, blank=True)
    long_description = models.TextField(max_length=512, blank=True)
    required_by_date = models.DateField(auto_now=True)
    approval_profile = models.CharField(max_length=100, blank=True)
    bo  = models.CharField(max_length=100, blank=True)

    downtime_start = models.DateTimeField(auto_now=True)
    planner  = models.CharField(max_length=100, blank=True)
    work_class = models.CharField(max_length=100, blank=True)
    work_category = models.CharField(max_length=100, blank=True)
    work_priority = models.IntegerField(default=1)
    requestor = models.CharField(max_length=100, blank=True)
    owning_access_group = models.CharField(max_length=100, blank=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    primary_phone = models.CharField(max_length=100, blank=True)
    mobile_phone = models.CharField(max_length=100, blank=True)
    home_phone = models.CharField(max_length=100, blank=True)
    node_id = models.CharField(max_length=100, blank=True)
    asset_id = models.CharField(max_length=100, blank=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_by = models.CharField(max_length=100, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.asset_id

class QuestionsValidValue(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    seq_valid = models.CharField(max_length=100, blank=True)
    code_valid = models.CharField(max_length=100, blank=True)
    short_text_valid = models.CharField(max_length=100, blank=True)
    text_valid = models.CharField(max_length=100, blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

class ServiceHistoriesQuestions(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    seq = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=True)
    short_text = models.CharField(max_length=100, blank=True)
    text = models.CharField(max_length=100, blank=True)
    style = models.CharField(max_length=100, blank=True)
    valid_value = models.ManyToManyField(QuestionsValidValue, null=True)
    respone = models.CharField(max_length=100, blank=True)
    response_check_box = models.CharField(max_length=100, blank=True)
    response_radio = models.CharField(max_length=100,blank=True)
    responseDate = models.DateField(null=True)
    response_datetime = models.DateTimeField(auto_now=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

class AssetLocationAssetListServiceHistories(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    service_history_type = models.CharField(max_length=100,blank=True)
    effective_datetime = models.DateTimeField(auto_now=True)
    start_date_time = models.DateTimeField(auto_now=True)
    end_date_time = models.DateTimeField(auto_now=True)
    comments = models.CharField(max_length=100, blank=True)
    failure_type = models.CharField(max_length=100, blank=True)
    failure_mode = models.CharField(max_length=100, blank=True)
    failure_repair = models.CharField(max_length=100, blank=True)
    failure_component = models.CharField(max_length=100, blank=True)
    failure_root_cause = models.CharField(max_length=100, blank=True)
    question = models.ManyToManyField(ServiceHistoriesQuestions, null=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

class WorkOrderActivityCompletionAssetLocationAssetList(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    node_id = models.CharField(max_length=100, blank=True)
    asset_id = models.CharField(max_length=100, blank=True)
    participation = models.CharField(max_length=100, blank=True)
    service_histories = models.ManyToManyField(AssetLocationAssetListServiceHistories, null=True)
    measurent_type = models.CharField(max_length=100, blank=True)
    reading_type = models.CharField(max_length=100, blank=True)
    current_value = models.CharField(max_length=100, blank=True)
    reading_datetime = models.DateTimeField(auto_now=True)

    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']

class WorkOrderActivityCompletion(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False)
    activityid = models.CharField(max_length=100, blank=True)
    completiondatetime = models.DateTimeField(auto_now=True)
    asset_location_asset_list = models.ManyToManyField(WorkOrderActivityCompletionAssetLocationAssetList, null=True)

    submitted_datetime = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering = ['-created_date']
