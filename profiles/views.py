from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from profiles.models import EncryptedProfile
from profiles.serializers import EncryptedProfileSerializer

from rest_framework import generics

class EncryptedProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated, )
    serializer_class = EncryptedProfileSerializer

    def get_object(self):
        try:
            return EncryptedProfile.objects.get(user=self.request.user)
        except EncryptedProfile.DoesNotExist:
            # Create if it does not exists.
            # This can only happen if a staff member deleted it.
            return EncryptedProfile.objects.create(
                user=self.request.user, data="")
