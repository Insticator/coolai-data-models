"""
Audience data models

Supports multiple platforms:
- Generic (platform-agnostic with performance ranks)
- Xandr (profile-based targeting)
- Meta (custom/lookalike audiences)
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List


# ============================================================================
# GENERIC AUDIENCE
# ============================================================================

class Audience(BaseModel):
    """Generic audience definition with performance metrics"""
    audience_id: Optional[str] = Field(None, description="Unique audience identifier")
    age: str = Field(..., description="Age group: 18-24, 25-34, 35-44, 45-54, 55-64, 65+, all")
    gender: str = Field(..., description="Gender: male, female, all")
    interest_group: str = Field(..., description="Interest group/segment")
    geography: str = Field(..., description="Geographic location")
    
    # Performance ranks (optional, added by ranking system)
    overall_rank: Optional[int] = Field(None, description="Overall combination rank")
    age_rank: Optional[int] = Field(None, description="Individual age rank")
    gender_rank: Optional[int] = Field(None, description="Individual gender rank")
    interest_rank: Optional[int] = Field(None, description="Individual interest rank")
    geography_rank: Optional[int] = Field(None, description="Individual geography rank")
    
    # Performance metrics (optional, added by ranking system)
    composite_score: Optional[float] = Field(None, description="Composite performance score")
    ctr: Optional[float] = Field(None, description="Click-through rate")
    cpm: Optional[float] = Field(None, description="Cost per thousand impressions")
    imps: Optional[int] = Field(None, description="Total impressions")
    
    @validator('age')
    def validate_age(cls, v):
        valid = ['18-24', '25-34', '35-44', '45-54', '55-64', '65+', 'all']
        if v not in valid:
            raise ValueError(f"age must be one of {valid}")
        return v
    
    @validator('gender')
    def validate_gender(cls, v):
        valid = ['male', 'female', 'all']
        if v not in valid:
            raise ValueError(f"gender must be one of {valid}")
        return v


# ============================================================================
# XANDR AUDIENCE
# ============================================================================

class XandrSegment(BaseModel):
    """Xandr segment definition"""
    segment_id: int = Field(..., description="Xandr segment ID")
    code: Optional[str] = Field(None, description="Segment code")
    name: Optional[str] = Field(None, description="Segment name")
    action: str = Field(default="include", description="include or exclude")


class XandrAudience(Audience):
    """Xandr profile-based audience targeting"""
    profile_id: Optional[int] = Field(None, description="Xandr profile ID")
    segments: Optional[List[XandrSegment]] = Field(default=[], description="Targeting segments")
    age_targets: Optional[List[str]] = Field(None, description="Age targeting (Xandr format)")
    gender_target: Optional[str] = Field(None, description="Gender targeting")
    geo_targets: Optional[List[dict]] = Field(None, description="Geographic targeting")


# ============================================================================
# META AUDIENCE
# ============================================================================

class MetaAudience(Audience):
    """Meta Ads custom/lookalike audience"""
    audience_type: str = Field(..., description="CUSTOM, LOOKALIKE, SAVED")
    facebook_audience_id: Optional[str] = Field(None, description="Meta audience ID")
    lookalike_spec: Optional[dict] = Field(None, description="Lookalike audience configuration")
    targeting: Optional[dict] = Field(None, description="Detailed targeting spec")
    
    @validator('audience_type')
    def validate_audience_type(cls, v):
        valid = ['CUSTOM', 'LOOKALIKE', 'SAVED']
        if v.upper() not in valid:
            raise ValueError(f"audience_type must be one of {valid}")
        return v.upper()

