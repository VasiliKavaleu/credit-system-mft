from rest_framework import viewsets
from rest_framework.response import Response

from credit_system import services
from credit_system.models import Contract
from credit_system.serializers import ContractListSerializer


class ContractViewSet(viewsets.ViewSet):
    lookup_url_kwarg = "contract_id"

    def list(self, request):
        queryset = Contract.objects.all()
        serializer = ContractListSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, contract_id=None):
        response_payload = services.get_manufacturer_ids_by_contract_number(contract_id)
        return Response(response_payload)
