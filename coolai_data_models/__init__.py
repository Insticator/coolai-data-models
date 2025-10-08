"""
CoolAI Data Models Package

Centralized Pydantic models for all CoolAI packages.
Each model type is in its own module with platform-specific variations.

Modules:
- campaign: Campaign, KPI, CampaignBase (+ Xandr, Meta variations)
- audience: Audience (+ Xandr, Meta variations)
- creative: Creative (+ Xandr, Meta variations)
- budget: BudgetRecommendation
- line_items: LineItem (+ Xandr, Meta variations)
- performance: PerformanceRecord
"""

# Campaign models
from .campaign import (
    KPI,
    CampaignBase,
    Campaign,
    XandrCampaign,
    MetaCampaign
)

# Audience models
from .audience import (
    Audience,
    XandrAudience,
    XandrSegment,
    MetaAudience
)

# Creative models
from .creative import (
    Creative,
    XandrCreative,
    MetaCreative,
    MetaCreativeAsset
)

# Budget models
from .budget import BudgetRecommendation

# Line item models
from .line_items import (
    LineItem,
    XandrLineItem,
    MetaAdSet
)

# Performance models
from .performance import PerformanceRecord

__version__ = "0.1.0"

# Generic models (platform-agnostic)
__all__ = [
    # Core models
    'Campaign',
    'CampaignBase',
    'KPI',
    'Audience',
    'Creative',
    'BudgetRecommendation',
    'LineItem',
    'PerformanceRecord',
    
    # Xandr models
    'XandrCampaign',
    'XandrAudience',
    'XandrSegment',
    'XandrCreative',
    'XandrLineItem',
    
    # Meta models
    'MetaCampaign',
    'MetaAudience',
    'MetaCreative',
    'MetaCreativeAsset',
    'MetaAdSet'
]

