from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import StateViewSet

from .apiviews import StateList, StateDetail, CasesList

router = DefaultRouter()
router.register('states', StateViewSet, base_name='states')

urlpatterns = [
    path("states/", StateList.as_view(), name="states_list"),
    path("states/<int:pk>/", StateDetail.as_view(), name="states_detail"),
    path("states/<int:pk>/choices/", CasesList.as_view(), name="cases_list"),
]

urlpatterns += router.urls
