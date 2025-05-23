from rest_framework import serializers
from .models import Domicile, Influencer, Category, RateCard, SocialPlatform

class DomicileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domicile
        fields = ["id", "city"]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class RateCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = RateCard
        fields = [ 'title', 'price']


class SocialPlatformSerializer(serializers.ModelSerializer):
    rate_cards = RateCardSerializer(many=True,required=False)

    class Meta:
        model = SocialPlatform
        fields = [
            "id",
            "platform",
            "profile_url",
            "username",
            "followers",
            "engagement_rate",
            "avg_likes_per_post",
            "avg_comments_per_post",
            "avg_views_per_post",
            "rate_cards"
        ]


class InfluencerSerializer2(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    social_platforms = SocialPlatformSerializer(many=True)
    domicile = serializers.CharField()  # Accept string input
    
    class Meta:
        model = Influencer
        fields = [
            "id",
            "full_name",
            "profile_picture",
            "domicile",
            "description",
            "email",
            "phone",
            "address",
            "categories",
            "social_platforms",
        ]
    
    def get_categories(self, obj):
        """Return categories as list of names"""
        return [category.name for category in obj.categories.all()]
    

    def create(self, validated_data):
        category_names = []
        if 'categories' in self.context:
            category_names = self.context['categories']
        elif hasattr(self, 'initial_data') and 'categories' in self.initial_data:
            category_names = self.initial_data['categories']
        
        platforms_data = validated_data.pop("social_platforms")
        domicile_city = validated_data.pop("domicile")

        domicile_obj, _ = Domicile.objects.get_or_create(city=domicile_city)
        validated_data["domicile"] = domicile_obj

        influencer = Influencer.objects.create(**validated_data)

        for name in category_names:
            category_obj, _ = Category.objects.get_or_create(name=name)
            influencer.categories.add(category_obj)

        for platform_data in platforms_data:
            rate_cards_data = platform_data.pop("rate_cards", [])
            social_platform = SocialPlatform.objects.create(
                influencer=influencer,
                **platform_data
            )
            for rc_data in rate_cards_data:
                RateCard.objects.create(social_platform=social_platform, **rc_data)

        return influencer

    
    def to_representation(self, instance):
        """Override to return domicile as string in output"""
        data = super().to_representation(instance)
        if instance.domicile:
            data['domicile'] = instance.domicile.city
        return data

class InfluencerSerializer(serializers.ModelSerializer):
    categories = serializers.SerializerMethodField()
    social_platforms = SocialPlatformSerializer(many=True)
    domicile = serializers.CharField()  # Accept string input
    
    class Meta:
        model = Influencer
        fields = [
            "id",
            "full_name",
            "profile_picture",
            "domicile",
            "description",
            "email",
            "phone",
            "address",
            "categories",
            "social_platforms",
        ]
    
    def get_categories(self, obj):
        """Return categories as list of names"""
        return [category.name for category in obj.categories.all()]
    
    def create(self, validated_data):
        # Extract categories from request data since it's not in validated_data anymore
        request_data = self.context['request'].data
        category_names = request_data.get('categories', [])
        
        platforms_data = validated_data.pop("social_platforms")
        domicile_city = validated_data.pop("domicile")
        
        # Get or create domicile
        domicile_obj, _ = Domicile.objects.get_or_create(city=domicile_city)
        validated_data["domicile"] = domicile_obj
        
        influencer = Influencer.objects.create(**validated_data)
        
        # Add categories by name
        for name in category_names:
            category_obj, _ = Category.objects.get_or_create(name=name)
            influencer.categories.add(category_obj)
        
        # Create social platforms
        for platform_data in platforms_data:
            SocialPlatform.objects.create(influencer=influencer, **platform_data)
        
        return influencer
    
    def to_representation(self, instance):
        """Override to return domicile as string in output"""
        data = super().to_representation(instance)
        if instance.domicile:
            data['domicile'] = instance.domicile.city
        return data
