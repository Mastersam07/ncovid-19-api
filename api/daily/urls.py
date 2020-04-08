from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import DailyList, DailyDetail

router = DefaultRouter()
router.register('api/states', DailyList, base_name='daily')

urlpatterns = [
    path("api/daily/", DailyList.as_view(), name="daily_list"),
    path("api/daily/<str:date>/", DailyDetail.as_view(), name="daily_detail"),
]

