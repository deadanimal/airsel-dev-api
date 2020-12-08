from datetime import datetime
from calendar import timegm
import json

from django.contrib.auth.forms import PasswordResetForm
from django.conf import settings
from django.utils.translation import gettext as _
from rest_framework import serializers
from django.utils.timezone import now

from .models import (
    OperationalReading,
    WorkRequest,
    WorkOrderActivityCompletionAssetLocationAssetList,
    AssetLocationAssetListServiceHistories,
    ServiceHistoriesQuestions,
    QuestionsValidValue,
    WorkOrderActivityCompletion
)

class OperationalReadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = OperationalReading
        fields = '__all__'

class WorkRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkRequest
        fields = '__all__'

class WorkOrderActivityCompletionAssetLocationAssetListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WorkOrderActivityCompletionAssetLocationAssetList
        fields = '__all__'

class AssetLocationAssetListServiceHistoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetLocationAssetListServiceHistories
        fields = '__all__'

class ServiceHistoriesQuestionsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceHistoriesQuestions
        fields = '__all__'

class QuestionsValidValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionsValidValue
        fields = '__all__'

class WorkOrderActivityCompletionSerializer(serializers.ModelSerializer):

	class Meta:
		model = WorkOrderActivityCompletion
		fields = '__all__'

class ServiceHistoriesQuestionsExtendedSerializer(serializers.ModelSerializer):
    
    valid_value = QuestionsValidValueSerializer(many=True)
    class Meta:
        model = ServiceHistoriesQuestions
        fields = '__all__'


class AssetLocationAssetListServiceHistoriesExtendedSerializer(serializers.ModelSerializer):
    
    question = ServiceHistoriesQuestionsExtendedSerializer(many=True)
    class Meta:
        model = AssetLocationAssetListServiceHistories
        fields = '__all__'

class WorkOrderActivityCompletionAssetLocationAssetListExtendedSerializer(serializers.ModelSerializer):

    service_histories = AssetLocationAssetListServiceHistoriesExtendedSerializer(many=True)
    class Meta:
        model = WorkOrderActivityCompletionAssetLocationAssetList
        fields = '__all__'

class WorkOrderActivityCompletionExtendedSerializer(serializers.ModelSerializer):

    asset_location_asset_list = WorkOrderActivityCompletionAssetLocationAssetListExtendedSerializer(many=True)
    class Meta:
        model = WorkOrderActivityCompletion
        fields = '__all__'