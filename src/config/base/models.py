from django.db import models


class AuditBaseModel(models.Model):
    """Base model for audit"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
