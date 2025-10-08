"""Basic usage examples for coolai-data-models"""

from coolai_data_models import (
    Campaign, KPI,
    Audience,
    Creative,
    BudgetRecommendation,
    LineItem
)

# Example 1: Create a campaign
print("Example 1: Campaign Creation")
print("=" * 60)

campaign = Campaign(
    campaign_id='CAMP_Q4_2025',
    name='Q4 Tech Campaign',
    advertiser='TechCorp',
    vertical='technology',
    objective='traffic',
    kpi=KPI(type='ctr', target=0.15),
    start_date='2025-10-01',
    end_date='2025-12-31'
)

print(f"✅ Campaign created: {campaign.campaign_id}")
print(f"   Vertical: {campaign.vertical}")
print(f"   Objective: {campaign.objective}")


# Example 2: Create audience
print("\n\nExample 2: Audience Creation")
print("=" * 60)

audience = Audience(
    audience_id='AUD_001',
    age='25-34',
    gender='male',
    interest_group='Tech Enthusiasts',
    geography='San Francisco',
    composite_score=0.85,
    overall_rank=1
)

print(f"✅ Audience created: {audience.audience_id}")
print(f"   Demographics: {audience.age} {audience.gender}")
print(f"   Interest: {audience.interest_group}")
print(f"   Score: {audience.composite_score}")


# Example 3: Create creative
print("\n\nExample 3: Creative Creation")
print("=" * 60)

creative = Creative(
    creative_id='CRE_001',
    ad_format='300x250',
    media_type='banner',
    width=300,
    height=250,
    engagement_score=0.92
)

print(f"✅ Creative created: {creative.creative_id}")
print(f"   Format: {creative.ad_format}")
print(f"   Engagement: {creative.engagement_score}")


# Example 4: Create budget recommendation
print("\n\nExample 4: Budget Recommendation")
print("=" * 60)

budget = BudgetRecommendation(
    recommended_budget=10000.0,
    min_budget=5000.0,
    max_budget=20000.0,
    confidence='medium',
    method='ml_model'
)

print(f"✅ Budget: ${budget.recommended_budget:,.2f}")
print(f"   Range: ${budget.min_budget:,.2f} - ${budget.max_budget:,.2f}")
print(f"   Confidence: {budget.confidence}")


# Example 5: Assemble complete campaign
print("\n\nExample 5: Complete Campaign Pipeline")
print("=" * 60)

campaign.audiences = [audience]
campaign.creatives = [creative]
campaign.budget_recommendation = budget
campaign.recommended_budget = budget.recommended_budget

print(f"✅ Complete campaign assembled:")
print(f"   Audiences: {len(campaign.audiences)}")
print(f"   Creatives: {len(campaign.creatives)}")
print(f"   Budget: ${campaign.recommended_budget:,.2f}")

print("\n" + "=" * 60)
print("✅ All models validated successfully!")
print("=" * 60)

