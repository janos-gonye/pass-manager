from rest_framework import routers

from profiles.views import EncryptedProfileViewSet

router = routers.SimpleRouter()
router.register('', EncryptedProfileViewSet, basename='profiles')

urlpatterns = router.urls
