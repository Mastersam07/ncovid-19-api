from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import DailyList, DailyDetail

router = DefaultRouter()
router.register('api/daily', DailyList, base_name='daily')

urlpatterns = [
    path("api/daily/", DailyList.as_view(), name="daily_list"),
    path("api/daily/<int:id>/", DailyDetail.as_view(), name="daily_detail"),
]

