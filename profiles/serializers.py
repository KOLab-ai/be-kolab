from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'role', 'fullname', 'email', 'company', 'position_title']
        read_only_fields = ['email']  # Email bisa di-read-only karena ambil dari user

    def create(self, validated_data):
        user = self.context['request'].user
        validated_data['email'] = user.email  # Optional, karena bisa redundant
        return Profile.objects.create(user=user, **validated_data)

    def update(self, instance, validated_data):
        # Optional: to prevent email update
        validated_data.pop('email', None)
        return super().update(instance, validated_data)
