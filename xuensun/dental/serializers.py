from rest_framework import serializers
from .models.data.layanan import Services

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        models = Services
        fields = '__all__'