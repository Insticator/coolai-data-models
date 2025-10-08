"""Tests for campaign models"""

import pytest
from coolai_data_models import Campaign, CampaignBase, KPI, XandrCampaign, MetaCampaign


def test_kpi_creation():
    """Test KPI model creation"""
    kpi = KPI(type='ctr', target=0.15)
    assert kpi.type == 'ctr'
    assert kpi.target == 0.15


def test_campaign_base_creation():
    """Test CampaignBase model creation"""
    campaign = CampaignBase(
        campaign_id='CAMP_001',
        name='Test Campaign',
        advertiser='Acme',
        vertical='technology',
        objective='traffic',
        kpi=KPI(type='ctr', target=0.15),
        start_date='2025-10-01',
        end_date='2025-12-31'
    )
    assert campaign.campaign_id == 'CAMP_001'
    assert campaign.vertical == 'technology'


def test_campaign_invalid_objective():
    """Test that invalid objective raises error"""
    with pytest.raises(ValueError, match="objective must be one of"):
        CampaignBase(
            campaign_id='CAMP_001',
            name='Test',
            advertiser='Acme',
            vertical='technology',
            objective='invalid',
            kpi=KPI(type='ctr', target=0.15),
            start_date='2025-10-01',
            end_date='2025-12-31'
        )


def test_complete_campaign():
    """Test Campaign model with components"""
    campaign = Campaign(
        campaign_id='CAMP_001',
        name='Test',
        advertiser='Acme',
        vertical='technology',
        objective='traffic',
        kpi=KPI(type='ctr', target=0.15),
        start_date='2025-10-01',
        end_date='2025-12-31'
    )
    
    # Components should be empty lists by default
    assert campaign.audiences == []
    assert campaign.creatives == []
    assert campaign.line_items == []


def test_xandr_campaign():
    """Test Xandr-specific campaign"""
    campaign = XandrCampaign(
        campaign_id='XANDR_001',
        name='Test',
        advertiser='Acme',
        vertical='technology',
        objective='traffic',
        kpi=KPI(type='ctr', target=0.15),
        start_date='2025-10-01',
        end_date='2025-12-31',
        advertiser_id=123,
        insertion_order_id=456
    )
    
    assert campaign.advertiser_id == 123
    assert campaign.insertion_order_id == 456

