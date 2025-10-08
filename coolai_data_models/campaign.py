"""
Campaign data models

Supports multiple platforms:
- Generic (platform-agnostic)
- Xandr
- Meta Ads
- Google Ads (future)
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List, Any, Dict
from datetime import datetime


# ============================================================================
# KPI MODELS
# ============================================================================

class KPI(BaseModel):
    """Campaign KPI definition"""
    type: str = Field(..., description="KPI type: ctr, cpm, cpa, conversion_rate")
    target: float = Field(..., description="Target value for the KPI")


# ============================================================================
# CAMPAIGN BASE
# ============================================================================

class CampaignBase(BaseModel):
    """Base campaign definition (platform-agnostic)"""
    campaign_id: str = Field(..., description="Unique campaign identifier")
    name: str = Field(..., description="Campaign name")
    advertiser: str = Field(..., description="Advertiser name")
    vertical: str = Field(..., description="Industry vertical")
    objective: str = Field(..., description="Campaign objective: awareness, traffic, conversions")
    kpi: KPI = Field(..., description="Campaign KPI")
    start_date: str = Field(..., description="Campaign start date")
    end_date: str = Field(..., description="Campaign end date")
    
    @validator('objective')
    def validate_objective(cls, v):
        valid = ['awareness', 'traffic', 'conversions']
        if v not in valid:
            raise ValueError(f"objective must be one of {valid}")
        return v
    
    @validator('vertical')
    def validate_vertical(cls, v):
        valid = ['technology', 'automotive', 'retail', 'finance', 'healthcare', 
                'education', 'travel_tourism', 'food_beverage', 'beauty_personal_care',
                'home_lifestyle', 'home_services', 'nonprofit', 'financial_services',
                'services', 'general']
        if v not in valid:
            raise ValueError(f"vertical must be one of {valid}")
        return v


class Campaign(CampaignBase):
    """
    Complete campaign with all components (platform-agnostic)
    
    This is populated progressively through the pipeline:
    1. Start with CampaignBase
    2. Add audiences (from coolai_audience)
    3. Add creatives (from coolai_creative)
    4. Add budget_recommendation (from coolai_budget)
    5. Add line_items (from coolai_line_items)
    """
    audiences: Optional[List[Any]] = Field(default=[], description="Recommended audiences")
    creatives: Optional[List[Any]] = Field(default=[], description="Selected creatives")
    budget_recommendation: Optional[Any] = Field(None, description="Budget recommendation")
    recommended_budget: Optional[float] = Field(None, description="Recommended budget value")
    line_items: Optional[List[Any]] = Field(default=[], description="Generated line items")


# ============================================================================
# PLATFORM-SPECIFIC CAMPAIGNS
# ============================================================================

class XandrCampaign(CampaignBase):
    """Xandr-specific campaign fields"""
    advertiser_id: Optional[int] = Field(None, description="Xandr advertiser ID")
    insertion_order_id: Optional[int] = Field(None, description="Xandr insertion order ID")
    state: Optional[str] = Field(None, description="Xandr campaign state")
    budget_intervals: Optional[List[dict]] = Field(None, description="Budget pacing intervals")


class MetaCampaign(CampaignBase):
    """Meta Ads-specific campaign fields"""
    account_id: Optional[str] = Field(None, description="Meta ad account ID")
    buying_type: Optional[str] = Field(None, description="AUCTION or RESERVED")
    bid_strategy: Optional[str] = Field(None, description="Bidding strategy")
    optimization_goal: Optional[str] = Field(None, description="Meta optimization goal")

