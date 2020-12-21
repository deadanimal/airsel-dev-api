from django.shortcuts import render
from django.db.models import Q
from django.utils import timezone
import datetime
import pytz

from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import viewsets, status
from rest_framework_extensions.mixins import NestedViewSetMixin

from django_filters.rest_framework import DjangoFilterBackend

from .models import (
    OperationalReading,
    WorkRequest,
    WorkOrderActivityCompletionAssetLocationAssetList,
    AssetLocationAssetListServiceHistories,
    ServiceHistoriesQuestions,
    QuestionsValidValue,
    WorkOrderActivityCompletion
)

from .serializers import (
    OperationalReadingSerializer,
    WorkRequestSerializer,
    WorkOrderActivityCompletionAssetLocationAssetListSerializer,
    AssetLocationAssetListServiceHistoriesSerializer,
    ServiceHistoriesQuestionsSerializer,
    QuestionsValidValueSerializer,
    WorkOrderActivityCompletionSerializer,
    WorkOrderActivityCompletionExtendedSerializer
)


class OperationalReadingViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = OperationalReading.objects.all()
    serializer_class = OperationalReadingSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = OperationalReading.objects.all()

        # FROM APPLICATION/JSON THROUGH API
        if bool(self.request.data):
            print("enter bool()")
            if 'from_date' in self.request.data and 'to_date' in self.request.data:

                from_date = self.request.data.get('from_date', None)
                to_date = self.request.data.get('to_date', None)

                if from_date is not None and to_date is not None:
                    # print(OperationalReading.objects.filter(submitted_datetime__range=(from_date,to_date)).query)
                    queryset = OperationalReading.objects.filter(submitted_datetime__range=(from_date,to_date))

        return queryset


class WorkRequestViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = WorkRequest.objects.all()
    serializer_class = WorkRequestSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = WorkRequest.objects.all()

        # FROM APPLICATION/JSON THROUGH API
        if bool(self.request.data):
            print("enter bool()")
            if 'from_date' in self.request.data and 'to_date' in self.request.data:

                from_date = self.request.data.get('from_date', None)
                to_date = self.request.data.get('to_date', None)

                if from_date is not None and to_date is not None:
                    # print(WorkRequest.objects.filter(submitted_datetime__range=(from_date,to_date)).query)
                    queryset = WorkRequest.objects.filter(submitted_datetime__range=(from_date,to_date))

        return queryset


class WorkOrderActivityCompletionAssetLocationAssetListViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = WorkOrderActivityCompletionAssetLocationAssetList.objects.all()
    serializer_class = WorkOrderActivityCompletionAssetLocationAssetListSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = WorkOrderActivityCompletionAssetLocationAssetList.objects.all()

        return queryset


class AssetLocationAssetListServiceHistoriesViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = AssetLocationAssetListServiceHistories.objects.all()
    serializer_class = AssetLocationAssetListServiceHistoriesSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = AssetLocationAssetListServiceHistories.objects.all()

        return queryset


class ServiceHistoriesQuestionsViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = ServiceHistoriesQuestions.objects.all()
    serializer_class = ServiceHistoriesQuestionsSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = ServiceHistoriesQuestions.objects.all()

        return queryset


class QuestionsValidValueViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = QuestionsValidValue.objects.all()
    serializer_class = QuestionsValidValueSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = QuestionsValidValue.objects.all()

        return queryset


class WorkOrderActivityCompletionViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
    queryset = WorkOrderActivityCompletion.objects.all()
    serializer_class = WorkOrderActivityCompletionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [AllowAny]
        else:
            permission_classes = [AllowAny]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        queryset = WorkOrderActivityCompletion.objects.all()

        # FROM APPLICATION/JSON THROUGH API
        if bool(self.request.data):
            print("enter bool()")
            if 'from_date' in self.request.data and 'to_date' in self.request.data:

                from_date = self.request.data.get('from_date', None)
                to_date = self.request.data.get('to_date', None)

                if from_date is not None and to_date is not None:
                    # print(WorkOrderActivityCompletion.objects.filter(submitted_datetime__range=(from_date,to_date)).query)
                    queryset = WorkOrderActivityCompletion.objects.filter(submitted_datetime__range=(from_date,to_date))

        return queryset

    @action(methods=['POST'], detail=False)
    def extended_all(self, request, *args, **kwargs):

        from_date = self.request.data['from_date']
        to_date = self.request.data['to_date']

        queryset = WorkOrderActivityCompletion.objects.all()

        if from_date is not None and to_date is not None:
            queryset = WorkOrderActivityCompletion.objects.filter(
                completiondatetime__range=(from_date, to_date))

        serializer = WorkOrderActivityCompletionExtendedSerializer(
            queryset, many=True)
        return Response(serializer.data)

    @action(methods=['GET'], detail=True)
    def extended(self, request, *args, **kwargs):
        work_order_activity = self.get_object()

        serializer = WorkOrderActivityCompletionExtendedSerializer(
            work_order_activity)
        return Response(serializer.data)
