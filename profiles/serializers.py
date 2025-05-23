from rest_framework import serializers
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'role', 'fullname', 'email', 'company', 'position_title']

    def create(self, validated_data):
        user = self.context['request'].user
        return Profile.objects.create(user=user, **validated_data)
