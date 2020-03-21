from django.contrib import admin

from profiles.models import EncryptedProfile

admin.site.register(EncryptedProfile)
