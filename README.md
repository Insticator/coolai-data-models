# CoolAI Data Models

**Centralized Pydantic models for the CoolAI ecosystem.**

Single source of truth for data structures across all CoolAI packages. Version number defines API compatibility.

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Pydantic V2](https://img.shields.io/badge/pydantic-v2-blue.svg)](https://docs.pydantic.dev/)

## Features

- **🎯 Platform-Agnostic**: Generic models work everywhere
- **🔌 Platform-Specific**: Xandr, Meta variations when needed
- **✅ Type-Safe**: Full Pydantic validation
- **📦 Modular**: One module per model type
- **🔄 Versionable**: Semantic versioning for API compatibility

## Installation

```bash
pip install coolai-data-models
```

## Quick Start

```python
from coolai_data_models import Campaign, KPI, Audience, Creative

# Create campaign
campaign = Campaign(
    campaign_id='CAMP_001',
    name='Q4 Campaign',
    advertiser='Acme Corp',
    vertical='technology',
    objective='traffic',
    kpi=KPI(type='ctr', target=0.15),
    start_date='2025-10-01',
    end_date='2025-12-31'
)

# Add components
campaign.audiences = [Audience(...)]
campaign.creatives = [Creative(...)]
```

## Models

### Campaign Models (`campaign.py`)

**Generic:**
- `KPI` - Key performance indicator
- `CampaignBase` - Base campaign definition
- `Campaign` - Complete campaign with components

**Platform-Specific:**
- `XandrCampaign` - Xandr insertion orders
- `MetaCampaign` - Meta ad campaigns

```python
from coolai_data_models import Campaign, XandrCampaign, MetaCampaign
```

### Audience Models (`audience.py`)

**Generic:**
- `Audience` - Age, gender, interests, geography with performance ranks

**Platform-Specific:**
- `XandrAudience` - Profile-based targeting with segments
- `XandrSegment` - Segment definition
- `MetaAudience` - Custom/lookalike audiences

```python
from coolai_data_models import Audience, XandrAudience, MetaAudience
```

### Creative Models (`creative.py`)

**Generic:**
- `Creative` - Ad format, size, engagement score

**Platform-Specific:**
- `XandrCreative` - Banner/video with audit status
- `MetaCreative` - Multi-asset ads (carousel, video)
- `MetaCreativeAsset` - Individual asset in Meta creative

```python
from coolai_data_models import Creative, XandrCreative, MetaCreative
```

### Budget Models (`budget.py`)

**Generic:**
- `BudgetRecommendation` - Min/max/recommended with confidence

```python
from coolai_data_models import BudgetRecommendation
```

### Line Item Models (`line_items.py`)

**Generic:**
- `LineItem` - Audience + Creative + budget allocation

**Platform-Specific:**
- `XandrLineItem` - Revenue type, daily/lifetime budget
- `MetaAdSet` - Optimization goal, billing event

```python
from coolai_data_models import LineItem, XandrLineItem, MetaAdSet
```

### Performance Models (`performance.py`)

**Generic:**
- `PerformanceRecord` - ETL and analytics data

```python
from coolai_data_models import PerformanceRecord
```

## Module Structure

```
coolai_data_models/
├── campaign.py          # Campaign, KPI models
├── audience.py          # Audience models
├── creative.py          # Creative models
├── budget.py            # Budget models
├── line_items.py        # Line item models
└── performance.py       # Performance data models
```

## Version Compatibility

| Version | Changes |
|---------|---------|
| 0.1.0   | Initial release - all base models |

## Platform Support

| Platform | Campaign | Audience | Creative | Line Item |
|----------|----------|----------|----------|-----------|
| Generic  | ✅        | ✅        | ✅        | ✅         |
| Xandr    | ✅        | ✅        | ✅        | ✅         |
| Meta     | ✅        | ✅        | ✅        | ✅         |
| Google   | 🔜        | 🔜        | 🔜        | 🔜         |

## Usage in Packages

```toml
# In your package's pyproject.toml
dependencies = [
    "coolai-data-models>=0.1.0,<0.2.0",  # Pin to compatible version
]
```

## Development

```bash
git clone https://github.com/Insticator/coolai-data-models.git
cd coolai-data-models
pip install -e ".[dev]"
pytest
```

## License

Proprietary - Insticator Inc.
