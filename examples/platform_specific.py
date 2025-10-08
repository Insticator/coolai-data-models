"""Platform-specific model examples"""

from coolai_data_models import (
    XandrCampaign, XandrAudience, XandrSegment, XandrCreative, XandrLineItem,
    MetaCampaign, MetaAudience, MetaCreative, MetaCreativeAsset, MetaAdSet,
    KPI
)

# ============================================================================
# XANDR EXAMPLES
# ============================================================================

print("XANDR PLATFORM EXAMPLES")
print("=" * 60)

# Xandr Campaign
xandr_campaign = XandrCampaign(
    campaign_id='XANDR_CAMP_001',
    name='Xandr Q4 Campaign',
    advertiser='TechCorp',
    vertical='technology',
    objective='traffic',
    kpi=KPI(type='ctr', target=0.15),
    start_date='2025-10-01',
    end_date='2025-12-31',
    advertiser_id=12345,
    insertion_order_id=67890,
    state='active'
)

print(f"✅ Xandr Campaign: {xandr_campaign.name}")
print(f"   Advertiser ID: {xandr_campaign.advertiser_id}")
print(f"   IO ID: {xandr_campaign.insertion_order_id}")

# Xandr Audience with segments
xandr_audience = XandrAudience(
    audience_id='XANDR_AUD_001',
    age='25-34',
    gender='male',
    interest_group='Tech',
    geography='US',
    profile_id=123,
    segments=[
        XandrSegment(segment_id=1001, name='Tech Buyers', action='include'),
        XandrSegment(segment_id=2002, name='Budget Shoppers', action='exclude')
    ]
)

print(f"\n✅ Xandr Audience: {xandr_audience.audience_id}")
print(f"   Profile ID: {xandr_audience.profile_id}")
print(f"   Segments: {len(xandr_audience.segments)}")

# Xandr Creative
xandr_creative = XandrCreative(
    creative_id='XANDR_CRE_001',
    ad_format='300x250',
    media_type='banner',
    width=300,
    height=250,
    engagement_score=0.85,
    xandr_creative_id=999,
    audit_status='approved',
    media_url='https://cdn.example.com/banner.jpg'
)

print(f"\n✅ Xandr Creative: {xandr_creative.creative_id}")
print(f"   Audit: {xandr_creative.audit_status}")


# ============================================================================
# META EXAMPLES
# ============================================================================

print("\n\nMETA PLATFORM EXAMPLES")
print("=" * 60)

# Meta Campaign
meta_campaign = MetaCampaign(
    campaign_id='META_CAMP_001',
    name='Meta Q4 Campaign',
    advertiser='TechCorp',
    vertical='technology',
    objective='traffic',
    kpi=KPI(type='ctr', target=0.15),
    start_date='2025-10-01',
    end_date='2025-12-31',
    account_id='act_123456',
    buying_type='AUCTION',
    bid_strategy='LOWEST_COST_WITHOUT_CAP',
    optimization_goal='LINK_CLICKS'
)

print(f"✅ Meta Campaign: {meta_campaign.name}")
print(f"   Account: {meta_campaign.account_id}")
print(f"   Goal: {meta_campaign.optimization_goal}")

# Meta Audience
meta_audience = MetaAudience(
    audience_id='META_AUD_001',
    age='25-34',
    gender='male',
    interest_group='Tech',
    geography='US',
    audience_type='LOOKALIKE',
    facebook_audience_id='123456789',
    lookalike_spec={'source_audience': 'base_audience', 'ratio': 0.01}
)

print(f"\n✅ Meta Audience: {meta_audience.audience_id}")
print(f"   Type: {meta_audience.audience_type}")
print(f"   FB ID: {meta_audience.facebook_audience_id}")

# Meta Creative
meta_creative = MetaCreative(
    creative_id='META_CRE_001',
    ad_format='carousel',
    media_type='banner',
    engagement_score=0.88,
    creative_type='CAROUSEL',
    assets=[
        MetaCreativeAsset(asset_type='IMAGE', url='https://example.com/img1.jpg'),
        MetaCreativeAsset(asset_type='IMAGE', url='https://example.com/img2.jpg')
    ],
    primary_text='Check out our products!',
    headline='Amazing Tech Deals',
    call_to_action='SHOP_NOW'
)

print(f"\n✅ Meta Creative: {meta_creative.creative_id}")
print(f"   Type: {meta_creative.creative_type}")
print(f"   Assets: {len(meta_creative.assets)}")

print("\n" + "=" * 60)
print("✅ All platform-specific models working!")
print("=" * 60)

