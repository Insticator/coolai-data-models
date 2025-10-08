"""
Line item data models

Combines audience + creative with budget allocation
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, Any


class LineItem(BaseModel):
    """Generic line item combining audience and creative"""
    line_item_id: str = Field(..., description="Unique line item identifier")
    audience_id: str = Field(..., description="Associated audience ID")
    creative_id: str = Field(..., description="Associated creative ID")
    audience: Any = Field(..., description="Full audience object")
    creative: Any = Field(..., description="Full creative object")
    combined_score: float = Field(..., description="Combined performance score")
    allocated_budget: float = Field(..., description="Allocated budget amount")
    
    @validator('combined_score')
    def validate_combined_score(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("combined_score must be between 0 and 1")
        return v
    
    @validator('allocated_budget')
    def validate_allocated_budget(cls, v):
        if v < 0:
            raise ValueError("allocated_budget must be positive")
        return v


class XandrLineItem(LineItem):
    """Xandr-specific line item configuration"""
    xandr_line_item_id: Optional[int] = Field(None, description="Xandr line item ID")
    insertion_order_id: Optional[int] = Field(None, description="Parent insertion order ID")
    revenue_type: Optional[str] = Field(None, description="CPM, CPC, CPA, etc.")
    revenue_value: Optional[float] = Field(None, description="Revenue/bid value")
    state: Optional[str] = Field(None, description="active or inactive")
    lifetime_budget: Optional[float] = Field(None, description="Lifetime budget")
    daily_budget: Optional[float] = Field(None, description="Daily budget cap")
    
    @validator('revenue_type')
    def validate_revenue_type(cls, v):
        if v is not None:
            valid = ['CPM', 'CPC', 'CPA', 'CPCV', 'VIEWABLE_CPM']
            if v.upper() not in valid:
                raise ValueError(f"revenue_type must be one of {valid}")
            return v.upper()
        return v


class MetaAdSet(LineItem):
    """Meta Ads AdSet (equivalent to line item)"""
    facebook_adset_id: Optional[str] = Field(None, description="Meta adset ID")
    campaign_id: str = Field(..., description="Parent campaign ID")
    optimization_goal: str = Field(..., description="REACH, LINK_CLICKS, CONVERSIONS, etc.")
    billing_event: str = Field(..., description="IMPRESSIONS, LINK_CLICKS, etc.")
    bid_amount: Optional[int] = Field(None, description="Bid amount in cents")
    daily_budget: Optional[int] = Field(None, description="Daily budget in cents")
    lifetime_budget: Optional[int] = Field(None, description="Lifetime budget in cents")
    status: Optional[str] = Field(None, description="ACTIVE, PAUSED, DELETED")
    
    @validator('optimization_goal')
    def validate_optimization_goal(cls, v):
        valid = ['REACH', 'LINK_CLICKS', 'IMPRESSIONS', 'CONVERSIONS', 'APP_INSTALLS',
                'VIDEO_VIEWS', 'ENGAGEMENT', 'LEAD_GENERATION']
        if v.upper() not in valid:
            raise ValueError(f"optimization_goal must be one of {valid}")
        return v.upper()

