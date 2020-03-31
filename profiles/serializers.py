from rest_framework import serializers

from profiles.models import EncryptedProfile


class EncryptedProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = EncryptedProfile
        fields = ('data', )
