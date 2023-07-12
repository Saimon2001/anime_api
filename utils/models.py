from django.db import models


class BaseModel(models.Model):
    estado = models.BooleanField(default=True)

    class Meta:
        abstract=True