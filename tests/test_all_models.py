"""Integration tests for all models"""

from coolai_data_models import (
    Audience, XandrAudience, MetaAudience,
    Creative, XandrCreative, MetaCreative, MetaCreativeAsset,
    BudgetRecommendation,
    LineItem,
    PerformanceRecord
)
from datetime import date


def test_audience_creation():
    """Test generic audience creation"""
    aud = Audience(
        age='25-34',
        gender='male',
        interest_group='Tech',
        geography='SF'
    )
    assert aud.age == '25-34'
    assert aud.audience_id is None  # Optional field


def test_creative_validation():
    """Test creative validation"""
    creative = Creative(
        creative_id='CRE_001',
        ad_format='300x250',
        media_type='banner',
        engagement_score=0.85
    )
    assert creative.engagement_score == 0.85


def test_budget_validation():
    """Test budget range validation"""
    budget = BudgetRecommendation(
        recommended_budget=10000,
        min_budget=5000,
        max_budget=20000,
        confidence='high',
        method='ml_model'
    )
    assert budget.min_budget < budget.recommended_budget < budget.max_budget


def test_performance_record():
    """Test performance record creation"""
    record = PerformanceRecord(
        advertiser_id=1,
        campaign_id=100,
        line_item_id=1000,
        campaign_vertical='technology',
        campaign_objective='traffic',
        campaign_kpi='ctr',
        ad_format='300x250',
        media_type='banner',
        device_type='mobile',
        age='25-34',
        gender='male',
        interest_group='Tech',
        geography='SF',
        impressions=10000,
        clicks=150,
        spend=25.50,
        conversion_rate=0.015,
        date=date(2025, 10, 1)
    )
    assert record.impressions == 10000
    assert record.clicks == 150


def test_platform_specific_models():
    """Test that platform-specific models work"""
    # Xandr
    xandr_aud = XandrAudience(
        age='all',
        gender='all',
        interest_group='Tech',
        geography='US',
        profile_id=123
    )
    assert xandr_aud.profile_id == 123
    
    # Meta
    meta_creative = MetaCreative(
        creative_id='META_CRE',
        ad_format='carousel',
        media_type='banner',
        engagement_score=0.9,
        creative_type='CAROUSEL',
        assets=[
            MetaCreativeAsset(asset_type='IMAGE', url='http://example.com/1.jpg')
        ]
    )
    assert len(meta_creative.assets) == 1


if __name__ == '__main__':
    test_audience_creation()
    test_creative_validation()
    test_budget_validation()
    test_performance_record()
    test_platform_specific_models()
    print("\n✅ All tests passed!")

