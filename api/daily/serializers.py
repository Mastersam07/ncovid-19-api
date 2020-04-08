from rest_framework import serializers

from .models import Daily


class DailySerializer(serializers.ModelSerializer):

    class Meta:
        model = Daily
        fields = ('No_of_cases', 'No_of_recovered', 'No_of_deaths')
