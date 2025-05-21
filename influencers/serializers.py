from rest_framework import serializers
from .models import Influencer, Category, SocialPlatform

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class SocialPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPlatform
        fields = [
            'id', 'platform', 'profile_url', 'username',
            'followers', 'engagement_rate',
            'avg_likes_per_post', 'avg_comments_per_post', 'avg_views_per_post'
        ]

class InfluencerSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True)
    social_platforms = SocialPlatformSerializer(many=True)

    class Meta:
        model = Influencer
        fields = [
            'id', 'full_name', 'domicile', 'description',
            'email', 'phone', 'address',
            'categories', 'social_platforms'
        ]

    def create(self, validated_data):
        categories_data = validated_data.pop('categories')
        platforms_data = validated_data.pop('social_platforms')
        influencer = Influencer.objects.create(**validated_data)

        for category in categories_data:
            cat_obj, _ = Category.objects.get_or_create(**category)
            influencer.categories.add(cat_obj)

        for platform in platforms_data:
            SocialPlatform.objects.create(influencer=influencer, **platform)

        return influencer
