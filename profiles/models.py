from django.contrib.auth import get_user_model
from django.db import models
from simple_history.models import HistoricalRecords


class EncryptedProfile(models.Model):
    user = models.OneToOneField(
        get_user_model(), on_delete=models.CASCADE)
    data = models.TextField(blank=True)
    history = HistoricalRecords()
