from rest_framework import generics, permissions
from .models import Profile
from .serializers import ProfileSerializer

class ProfileCreateUpdateView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        # Ambil profil milik user yang sedang login
        return self.request.user.profile
