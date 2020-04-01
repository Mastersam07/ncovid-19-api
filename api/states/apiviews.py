from rest_framework import generics, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from .models import State, Cases
from .serializers import StateSerializer, CaseSerializer


class StateList(APIView):
    @staticmethod
    def get(request):
        polls = State.objects.all()[:36]
        data = StateSerializer(polls, many=True).data
        return Response(data)


class StateDetail(APIView):
    @staticmethod
    def get(request, pk):
        state = get_object_or_404(State, pk=pk)
        data = StateSerializer(state).data
        return Response(data)


class CasesList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Cases.objects.filter(poll_id=self.kwargs["pk"])
        return queryset

    serializer_class = CaseSerializer


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
