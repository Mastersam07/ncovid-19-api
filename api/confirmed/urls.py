from django.urls import path
from rest_framework.routers import DefaultRouter

from .apiviews import CategoryList

router = DefaultRouter()
router.register('api/confirmed', CategoryList, base_name='states')

urlpatterns = [
    path("api/confirmed/", CategoryList.as_view(), name="confirmed"),
]

# urlpatterns += router.urls
