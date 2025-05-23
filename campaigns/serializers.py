from rest_framework import serializers
from .models import Campaign, Domicile, Category

class CampaignSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    target_locations = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Domicile.objects.all()
    )
    target_interests = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Campaign
        fields = '__all__'
