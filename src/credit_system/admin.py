from django.contrib import admin

from credit_system import models


admin.site.register(models.Item)
admin.site.register(models.Contract)
admin.site.register(models.CreditItem)
admin.site.register(models.CreditApplication)
admin.site.register(models.Manufacturer)
