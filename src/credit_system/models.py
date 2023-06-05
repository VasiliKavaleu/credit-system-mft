from django.db import models

from config.base.models import AuditBaseModel


class Contract(AuditBaseModel):
    number = models.CharField(max_length=255, db_index=True, verbose_name="Number")
    credit_application = models.OneToOneField(
        "CreditApplication", on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = "Contract"
        verbose_name_plural = "Contracts"

    def __str__(self):
        return self.number


class CreditApplication(AuditBaseModel):
    number = models.CharField(max_length=255, db_index=True, verbose_name="Number")
    description = models.TextField(verbose_name="Description", null=True, blank=True)
    items = models.ManyToManyField(
        "Item", through="CreditItem", related_name="credit_applications"
    )

    def __str__(self):
        return f"Credit Application #{self.number}"


class CreditItem(AuditBaseModel):
    DEFAULT_QUANTITY = 1

    item = models.ForeignKey("Item", on_delete=models.CASCADE)
    credit_application = models.ForeignKey(
        "CreditApplication", on_delete=models.CASCADE
    )
    quantity = models.PositiveIntegerField(
        verbose_name="Quantity", default=DEFAULT_QUANTITY
    )

    class Meta:
        verbose_name = "Credit Item"
        verbose_name_plural = "Credit Items"
        unique_together = ["item", "credit_application"]

    def __str__(self):
        return f"Item: {self.item.title}, quantity: {self.quantity}"


class Item(AuditBaseModel):
    title = models.CharField(max_length=255, db_index=True, verbose_name="Title")
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, related_name="items"
    )

    class Meta:
        verbose_name = "Item"
        verbose_name_plural = "Items"

    def __str__(self):
        return self.title


class Manufacturer(AuditBaseModel):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Name")

    class Meta:
        verbose_name = "Manufacturer"
        verbose_name_plural = "Manufacturers"

    def __str__(self):
        return self.name
