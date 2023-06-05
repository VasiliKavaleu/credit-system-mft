from typing import TypedDict, List

from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import F

from credit_system.models import CreditApplication


class UniqueManufacturerIds(TypedDict):
    manufacturer_ids: List[int]


def get_manufacturer_ids_by_contract_number(contract_id: str) -> UniqueManufacturerIds:
    manufacturers = CreditApplication.objects.filter(
        contract__id=contract_id
    ).aggregate(manufacturer_ids=ArrayAgg("items__manufacturer", distinct=True))
    return manufacturers


def get_manufacturer_ids_by_contract_number2(contract_id: str) -> UniqueManufacturerIds:
    credit_applications = (
        CreditApplication.objects.filter(contract__id=contract_id)
        .only("number")
        .annotate(manufacturer_id=F("items__manufacturer"))
        .distinct("items__manufacturer")
    )

    return dict(
        manufacturer_ids=[
            credit_app.manufacturer_id for credit_app in credit_applications
        ]
    )


def get_manufacturer_ids_by_contract_number3(contract_id: str) -> UniqueManufacturerIds:
    credit_applications = (
        CreditApplication.objects.filter(contract__id=contract_id)
        .only("number")
        .annotate(manufacturer_ids=ArrayAgg("items__manufacturer", distinct=True))
    )

    return dict(
        manufacturer_ids=credit_applications[0].manufacturer_ids
        if credit_applications
        else []
    )
