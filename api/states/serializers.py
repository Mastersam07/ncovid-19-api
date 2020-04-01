from rest_framework import serializers

from .models import State, Cases


class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cases
        fields = '__all__'


class StateSerializer(serializers.ModelSerializer):
    cases = CaseSerializer(many=True, read_only=True, required=False)

    class Meta:
        model = State
        fields = '__all__'
