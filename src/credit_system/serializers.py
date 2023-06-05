from rest_framework import serializers

from credit_system.models import Contract


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = ["id", "number"]
