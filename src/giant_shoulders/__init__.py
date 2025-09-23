"""
Giant Shoulders - Strategic Open Source Discovery System
"""

from .models import GitHubProject, StrategicProfile, ContributionOpportunity, DiscoveryResult
from .discovery import GitHubStrategicScanner

__version__ = "0.1.0"
__all__ = [
    "GitHubProject",
    "StrategicProfile", 
    "ContributionOpportunity",
    "DiscoveryResult",
    "GitHubStrategicScanner"
]

