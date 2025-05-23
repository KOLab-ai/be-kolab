from campaigns.models import Campaign
from influencers.models import Influencer
from influencers.serializers import InfluencerSerializer
from core.chroma import chroma_collection
import openai


def generate_query(campaign, locations, categories_data):
    prompt = (
        "Create a concise search query for an influencer marketing campaign with the following details:\n"
        f"Goal: {campaign.campaign_goal}\n"
        f"Preferred Social Media: {campaign.prefer_sosmed}\n"
        f"Target Gender: {campaign.gender}\n"
        f"Target Age Range: {campaign.umur}\n"
        f"Target Locations: {', '.join(locations) if locations else 'None'}\n"
        f"Target Interests/Categories: {', '.join(categories_data) if categories_data else 'None'}\n"
        f"Product Category: {campaign.category_product}\n"
        "Return a short, focused search query string combining the key points to find suitable influencers, "
        "and include an inferred influencer persona (e.g., mom, student, beauty enthusiast, dad/father,  etc.) directly within the query itself."
    )

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful assistant that creates search queries for chroma DB.",
            },
            {"role": "user", "content": prompt},
        ],
    )

    return str(response.choices[0].message.content)


def get_recomendations(campaign: Campaign):
    target_interests = campaign.target_interests.all()
    target_locations = campaign.target_locations.all()

    locations = [dom.city for dom in target_locations]
    categories_data = [cat.name for cat in target_interests]

    query_text = generate_query(campaign, locations, categories_data)
    print(f"query_text: {query_text}\n\n")
    category_filters = [{f"category_{cat}": True} for cat in categories_data]

    metadata_filter = {
        "$and": [
            {"domicile": {"$in": locations}},
            {"$or": category_filters}
        ]
    }

    if len(category_filters) > 1:
        metadata_filter = {
            "$and": [
                {"domicile": {"$in": locations}},
                {"$or": category_filters}
            ]
        }
    elif len(category_filters) == 1:
        # No need for $or if only one filter
        metadata_filter = {
            "$and": [
                {"domicile": {"$in": locations}},
                category_filters[0]
            ]
        }
    else:
        # No categories, just filter on domicile
        metadata_filter = {
            "domicile": {"$in": locations}
        }

    # metadata_filter = {"domicile": {"$in": locations}}

    results = chroma_collection.query(
        query_texts=[query_text], n_results=5, 
        where=metadata_filter
    )
    print(results)
    metadata_list = results.get("metadatas", [[]])[0]
    influencer_ids = [meta["id"] for meta in metadata_list if "id" in meta]

    influencers = Influencer.objects.filter(id__in=influencer_ids)

    serialized = InfluencerSerializer(influencers, many=True).data
    return serialized
