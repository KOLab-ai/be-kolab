from django.contrib import admin
from .models import Category, Domicile, Influencer, SocialPlatform


@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    list_display = [
        "full_name",
        "domicile",
        "description",
        "email",
        "phone",
        "address",
        # "categories",
    ]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(Domicile)
class DomicileAdmin(admin.ModelAdmin):
    list_display = ["city"]


@admin.register(SocialPlatform)
class SocialPlatformAdmin(admin.ModelAdmin):
    list_display = [
        "platform",
        "profile_url",
        "username",
        "followers",
        "engagement_rate",
        "avg_likes_per_post",
        "avg_comments_per_post",
        "avg_views_per_post",
    ]
