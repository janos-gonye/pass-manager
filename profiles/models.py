from django.contrib.auth import get_user_model
from django.db import models
from simple_history.models import HistoricalRecords


class EncryptedProfile(models.Model):
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, null=True)
    data = models.TextField()
    history = HistoricalRecords()
