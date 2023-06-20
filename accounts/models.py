import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class ProjectUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.email

    class Meta:
        indexes = [models.Index(fields=["id"])]
