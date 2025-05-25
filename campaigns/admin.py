from django.contrib import admin

from campaigns.models import Campaign

# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
            "title",
        "campaign_goals",
        "social_platforms",
        "budget_range",
        "timeline",
        "target_age_range",
        "target_gender",
        # "target_locations",
        # "target_interests",
        "preferred_platforms",
        "product_category",
        "product_description",
    ]
