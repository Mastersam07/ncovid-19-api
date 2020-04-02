from django.urls import path
from rest_framework.routers import DefaultRouter
from .apiviews import StateViewSet

from .apiviews import StateList, StateDetail  # CasesList

router = DefaultRouter()
router.register('api/states', StateViewSet, base_name='states')

urlpatterns = [
    path("api/states/", StateList.as_view(), name="states_list"),
    path("api/states/<int:id>/", StateDetail.as_view(), name="states_detail"),
    # path("api/states/<int:id>/cases/", CasesList.as_view(), name="cases_list"),
]

urlpatterns += router.urls
