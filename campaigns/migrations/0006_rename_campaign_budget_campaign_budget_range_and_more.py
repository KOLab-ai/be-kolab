# Generated by Django 5.2.1 on 2025-05-25 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campaigns', '0005_campaign_recommended_influencers_matchingreport'),
    ]

    operations = [
        migrations.RenameField(
            model_name='campaign',
            old_name='campaign_budget',
            new_name='budget_range',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='category_product',
            new_name='product_category',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='description_product',
            new_name='product_description',
        ),
        migrations.RenameField(
            model_name='campaign',
            old_name='campaign_timeline',
            new_name='timeline',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='campaign_goal',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='prefer_sosmed',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='target_socialmedia',
        ),
        migrations.RemoveField(
            model_name='campaign',
            name='umur',
        ),
        migrations.AddField(
            model_name='campaign',
            name='campaign_goals',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='campaign',
            name='preferred_platforms',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='campaign',
            name='social_platforms',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='campaign',
            name='target_age_range',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='campaign',
            name='target_gender',
            field=models.JSONField(default=list),
        ),
    ]
