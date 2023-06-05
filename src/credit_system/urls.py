from rest_framework import routers

from credit_system import views


router = routers.DefaultRouter()

router.register("contracts", views.ContractViewSet, basename="contracts")
