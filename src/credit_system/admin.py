from django.contrib import admin

from credit_system import models


admin.site.register(models.Item)
admin.site.register(models.CreditApplication)


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ("pk", "number")


@admin.register(models.Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")


@admin.register(models.CreditItem)
class CreditItemAdmin(admin.ModelAdmin):
    list_display = ("pk", "credit_application", "item")
