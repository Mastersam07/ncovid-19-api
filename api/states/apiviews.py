from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Data
from .serializers import StateSerializer  # CaseSerializer


class StateList(APIView):
    @staticmethod
    def get(request):
        states = Data.objects.all()
        data = StateSerializer(states, many=True).data
        return Response(data)


class StateDetail(APIView):
    @staticmethod
    def get(request, id):
        state = get_object_or_404(Data, pk=id)
        data = StateSerializer(state).data
        return Response(data)


class StateViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = StateSerializer
