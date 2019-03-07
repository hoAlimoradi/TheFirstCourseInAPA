from rest_framework import serializers
from RestApp.models import Factor

class FactorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factor
        fields = ('id', 'name', 'description', 'total', 'paid')
