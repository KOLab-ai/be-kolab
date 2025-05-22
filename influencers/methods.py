import json

from dotenv import load_dotenv

from influencers.serializers import InfluencerSerializer, InfluencerSerializer2
from core.chroma import collection
import openai

load_dotenv()


def generate_description(influencer) -> str:
    prompt = f"""Write a short, friendly 1-sentence summary of this creator in third person perspective, highlighting the uniqueness of the creator:
- Name: {influencer.full_name}
- Location: {influencer.domicile}
- Bio: {influencer.description}
- Categories: {", ".join(cat.name for cat in influencer.categories.all())}
- Social Platforms: {", ".join(sp.platform for sp in influencer.social_platforms.all() if sp.platform)}
"""

    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return str(response.choices[0].message.content)


# Add this to your methods.py file or update your existing function
def proccess_influencer_data():
    # Insert Ke DB
    with open("influencers.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    
    for item in data:
        # Pass categories through context
        context = {'categories': item.get('categories', [])}
        serializer = InfluencerSerializer2(data=item, context=context)
        
        if serializer.is_valid():
            influencer = serializer.save()
            print(f"Saved: {item['full_name']}")
            
            # summary = generate_description(influencer)
            # # Insert Chroma
            # collection.add(
            #     documents=[summary],
            #     ids=[str(influencer.id)],  # Make sure ID is string
            #     metadatas=[
            #         {
            #             "id": str(influencer.id),
            #             "full_name": influencer.full_name,
            #             "domicile": str(influencer.domicile),  # Convert to string
            #             "categories": ",".join(
            #                 cat.name for cat in influencer.categories.all()
            #             ),
            #         }
            #     ],
            # )
        else:
            print(f"Error for {item['full_name']}: {serializer.errors}")
