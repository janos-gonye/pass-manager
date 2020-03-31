from django.urls import path

from profiles.views import EncryptedProfileView

urlpatterns = [
    path('', EncryptedProfileView.as_view()),
]
