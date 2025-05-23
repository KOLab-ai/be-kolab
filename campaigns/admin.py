from django.contrib import admin

from campaigns.models import Campaign

# Register your models here.


@admin.register(Campaign)
class CampaignAdmin(admin.ModelAdmin):
    list_display = [
        "campaign_goal",
        "campaign_budget",
        "campaign_timeline",
        "target_socialmedia",
        "prefer_sosmed",
        "gender",
        "umur",
        # "target_locations",
        # "target_interests",
        "category_product",
        "description_product",
    ]
