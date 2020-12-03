from datetime import datetime, timedelta

from django.conf import settings
from django.conf.urls import include, url
from django.contrib.gis import admin

from rest_framework import routers
from rest_framework_extensions.routers import NestedRouterMixin

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

from users.views import (
    MyTokenObtainPairView
)

class NestedDefaultRouter(NestedRouterMixin, routers.DefaultRouter):
    pass

router = NestedDefaultRouter()

# Assets app
from assets.views import (
    AssetLocationViewSet,
    AssetMeasurementTypeViewSet,
    AssetAttributeViewSet,
    AssetViewSet
)

# asset_location_cost_centers_router = router.register(
#     'asset-location-cost-centers', AssetLocationViewSet
# )
#
# asset_location_criticalitys_router = router.register(
#     'asset-location-criticalities', AssetLocationCriticalityReasonViewSet
# )

asset_locations_router = router.register(
    'asset-locations', AssetLocationViewSet
)

asset_measurement_types_router = router.register(
    'asset-measurement-types', AssetMeasurementTypeViewSet
)

asset_attributes_router = router.register(
    'asset-attributes', AssetAttributeViewSet
)

assets_router = router.register(
    'assets', AssetViewSet
)

# Operations app

from operations.views import (
    OperationalReadingViewSet,
    WorkRequestViewSet,
    WorkOrderActivityCompletionAssetLocationAssetListViewSet,
    AssetLocationAssetListServiceHistoriesViewSet,
    ServiceHistoriesQuestionsViewSet,
    QuestionsValidValueViewSet,
    WorkOrderActivityCompletionViewSet
)

operational_readings_router = router.register(
    'operational-readings', OperationalReadingViewSet
)

work_requests_router = router.register(
    'work-requests', WorkRequestViewSet
)

work_order_activity_completion_router = router.register(
    'work-order-activity-completion', WorkOrderActivityCompletionViewSet
)

work_order_activity_completion_asset_location_asset_list_router = router.register(
    'work-order-activity-completion-asset-location-asset-list', WorkOrderActivityCompletionAssetLocationAssetListViewSet
)

asset_location_asset_list_service_histories_router = router.register(
    'asset-location-asset-list-service-histories', AssetLocationAssetListServiceHistoriesViewSet
)

service_histories_questions_router = router.register(
    'service-histories-questions', ServiceHistoriesQuestionsViewSet
)

questions_valid_value_router = router.register(
    'questions-value-valid', QuestionsValidValueViewSet
)

# Wams app

from wams.views import (
    WamsViewSet
)

wams_router = router.register(
    'wams', WamsViewSet
)

# Organisations app

from organisations.views import (
    OrganisationViewSet
)

organisations_router = router.register(
    'organisations', OrganisationViewSet
)

# Users app

from users.views import (
    CustomUserViewSet
)

users_router = router.register(
    'users', CustomUserViewSet
)

urlpatterns = [
    url(r'v1/', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/registration/', include('rest_auth.registration.urls')),

    url('auth/obtain/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    url('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    url('auth/verify/', TokenVerifyView.as_view(), name='token_verify')
]
