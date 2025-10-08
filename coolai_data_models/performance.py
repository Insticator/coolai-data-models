"""
Performance data models

Used by ETL and analytics systems
"""

from pydantic import BaseModel, Field
from datetime import date as date_type
from typing import Optional


class PerformanceRecord(BaseModel):
    """Single performance record from raw data"""
    advertiser_id: int = Field(..., description="Advertiser ID")
    campaign_id: int = Field(..., description="Campaign ID")
    line_item_id: int = Field(..., description="Line item ID")
    
    # Campaign metadata
    campaign_vertical: str = Field(..., description="Campaign vertical")
    campaign_objective: str = Field(..., description="Campaign objective")
    campaign_kpi: str = Field(..., description="Campaign KPI type")
    
    # Creative attributes
    ad_format: str = Field(..., description="Ad format")
    media_type: str = Field(..., description="Media type")
    device_type: str = Field(..., description="Device type")
    
    # Audience attributes
    age: str = Field(..., description="Age group")
    gender: str = Field(..., description="Gender")
    interest_group: str = Field(..., description="Interest group")
    geography: str = Field(..., description="Geography")
    
    # Performance metrics
    impressions: int = Field(..., ge=0, description="Number of impressions")
    clicks: int = Field(..., ge=0, description="Number of clicks")
    spend: float = Field(..., ge=0, description="Spend amount")
    conversion_rate: float = Field(..., ge=0, description="Conversion rate")
    
    # Optional fields
    language: Optional[str] = Field(None, description="Language")
    engagement_score: Optional[int] = Field(None, description="Engagement score")
    date: date_type = Field(..., description="Date of record")

