from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from simple_history.models import HistoricalRecords


class User(AbstractUser):
    history = HistoricalRecords()


@receiver(post_save, sender=User)
def create_user_encrypted_profile_on_user_created(sender, instance,
                                                  created, **kwargs):
    from profiles.models import EncryptedProfile
    if not created:
        return
    EncryptedProfile.objects.create(user=instance, data='')
