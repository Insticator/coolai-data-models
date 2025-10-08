# Changelog

All notable changes to coolai-data-models will be documented in this file.

## [0.1.0] - 2025-10-08

### Added
- Initial release with modular model structure
- **Campaign models** (`campaign.py`):
  - `KPI`, `CampaignBase`, `Campaign`
  - `XandrCampaign`, `MetaCampaign` platform variations
- **Audience models** (`audience.py`):
  - `Audience` with performance ranks
  - `XandrAudience` with segment targeting
  - `MetaAudience` with custom/lookalike support
- **Creative models** (`creative.py`):
  - `Creative` generic asset
  - `XandrCreative` with audit status
  - `MetaCreative` with multi-asset support
- **Budget models** (`budget.py`):
  - `BudgetRecommendation` with confidence metrics
- **Line Item models** (`line_items.py`):
  - `LineItem` generic
  - `XandrLineItem` with revenue types
  - `MetaAdSet` with optimization goals
- **Performance models** (`performance.py`):
  - `PerformanceRecord` for ETL/analytics
- Full Pydantic v2 validation
- Platform-specific model variations
- Comprehensive documentation

### Dependencies
- pydantic >= 2.0.0

[0.1.0]: https://github.com/Insticator/coolai-data-models/releases/tag/v0.1.0

