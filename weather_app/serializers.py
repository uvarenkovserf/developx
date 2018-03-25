from rest_framework import serializers

from .models import GeoPosition, WeatherEntry, AverageStats


class GeoPositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = GeoPosition
        fields = '__all__'


class WeatherEntrySerializer(serializers.ModelSerializer):

    class Meta:
        model = WeatherEntry
        fields = '__all__'


class AverageStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = AverageStats
        fields = '__all__'
