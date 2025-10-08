"""
Creative data models

Supports multiple platforms:
- Generic (platform-agnostic)
- Xandr (banner/video creatives)
- Meta (carousel/video/image ads)
"""

from pydantic import BaseModel, Field, validator
from typing import Optional, List


# ============================================================================
# GENERIC CREATIVE
# ============================================================================

class Creative(BaseModel):
    """Generic creative asset definition"""
    creative_id: str = Field(..., description="Unique creative identifier")
    ad_format: str = Field(..., description="Ad format: 300x250, 728x90, video, etc.")
    media_type: str = Field(..., description="Media type: banner, video, native")
    width: Optional[int] = Field(None, description="Creative width in pixels")
    height: Optional[int] = Field(None, description="Creative height in pixels")
    engagement_score: float = Field(..., description="Expected engagement score (0-1)")
    
    @validator('media_type')
    def validate_media_type(cls, v):
        valid = ['banner', 'video', 'native', 'audio']
        if v not in valid:
            raise ValueError(f"media_type must be one of {valid}")
        return v
    
    @validator('engagement_score')
    def validate_engagement_score(cls, v):
        if not 0 <= v <= 1:
            raise ValueError("engagement_score must be between 0 and 1")
        return v


# ============================================================================
# XANDR CREATIVE
# ============================================================================

class XandrCreative(Creative):
    """Xandr-specific creative fields"""
    xandr_creative_id: Optional[int] = Field(None, description="Xandr creative ID")
    template_id: Optional[int] = Field(None, description="Xandr template ID")
    creative_format: Optional[str] = Field(None, description="Xandr creative format")
    audit_status: Optional[str] = Field(None, description="Audit status: pending, approved, rejected")
    ssl_status: Optional[str] = Field(None, description="SSL status: approved, pending")
    media_url: Optional[str] = Field(None, description="Media asset URL")
    click_url: Optional[str] = Field(None, description="Click-through URL")
    
    @validator('audit_status')
    def validate_audit_status(cls, v):
        if v is not None:
            valid = ['pending', 'approved', 'rejected', 'audited']
            if v not in valid:
                raise ValueError(f"audit_status must be one of {valid}")
        return v


# ============================================================================
# META CREATIVE
# ============================================================================

class MetaCreativeAsset(BaseModel):
    """Individual asset in Meta creative"""
    asset_type: str = Field(..., description="IMAGE, VIDEO, or CAROUSEL")
    url: str = Field(..., description="Asset URL")
    hash: Optional[str] = Field(None, description="Meta asset hash")


class MetaCreative(Creative):
    """Meta Ads creative with multi-asset support"""
    facebook_creative_id: Optional[str] = Field(None, description="Meta creative ID")
    creative_type: str = Field(..., description="SINGLE_IMAGE, VIDEO, CAROUSEL, etc.")
    assets: List[MetaCreativeAsset] = Field(..., description="Creative assets")
    primary_text: Optional[str] = Field(None, description="Ad primary text")
    headline: Optional[str] = Field(None, description="Ad headline")
    description: Optional[str] = Field(None, description="Ad description")
    call_to_action: Optional[str] = Field(None, description="CTA button type")
    
    @validator('creative_type')
    def validate_creative_type(cls, v):
        valid = ['SINGLE_IMAGE', 'VIDEO', 'CAROUSEL', 'SLIDESHOW', 'COLLECTION']
        if v.upper() not in valid:
            raise ValueError(f"creative_type must be one of {valid}")
        return v.upper()

