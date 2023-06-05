from django.contrib import admin
from django.urls import path, include

from credit_system.urls import router as credit_service_router


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(credit_service_router.urls)),
]
