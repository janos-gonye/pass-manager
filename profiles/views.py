from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from profiles.models import EncryptedProfile
from profiles.serializers import EncryptedProfileSerializer


class EncryptedProfileViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    serializer_class = EncryptedProfileSerializer

    def get_queryset(self):
        return EncryptedProfile.objects.filter(user_id=self.request.user.id)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
