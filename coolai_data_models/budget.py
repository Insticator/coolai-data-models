"""
Budget data models

Platform-agnostic budget recommendations
"""

from pydantic import BaseModel, Field, validator
from typing import Optional


class BudgetRecommendation(BaseModel):
    """Budget recommendation with confidence metrics"""
    recommended_budget: float = Field(..., description="Recommended budget amount")
    min_budget: float = Field(..., description="Minimum budget amount")
    max_budget: float = Field(..., description="Maximum budget amount")
    confidence: str = Field(..., description="Confidence level: low, medium, high")
    method: str = Field(..., description="Method used: rule_based, ml_model, historical")
    
    @validator('confidence')
    def validate_confidence(cls, v):
        valid = ['low', 'medium', 'high']
        if v not in valid:
            raise ValueError(f"confidence must be one of {valid}")
        return v
    
    @validator('recommended_budget', 'min_budget', 'max_budget')
    def validate_positive(cls, v):
        if v < 0:
            raise ValueError("Budget values must be positive")
        return v
    
    @validator('max_budget')
    def validate_max_greater_than_min(cls, v, values):
        if 'min_budget' in values and v < values['min_budget']:
            raise ValueError("max_budget must be greater than or equal to min_budget")
        return v

