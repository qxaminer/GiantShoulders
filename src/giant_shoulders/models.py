"""
Core data models for Giant Shoulders strategic open source discovery system.
"""

from dataclasses import dataclass
from typing import List, Optional
from datetime import datetime


@dataclass
class GitHubProject:
    """Represents a GitHub project with strategic analysis data"""
    name: str
    owner: str
    description: str
    url: str
    language: str
    stars: int
    forks: int
    issues_count: int
    last_updated: str
    topics: List[str] = None
    contributors_count: Optional[int] = None
    license: Optional[str] = None
    strategic_score: Optional[float] = None
    learning_alignment: Optional[float] = None
    contribution_opportunities: List[str] = None

    def __post_init__(self):
        if self.topics is None:
            self.topics = []
        if self.contribution_opportunities is None:
            self.contribution_opportunities = []


@dataclass
class StrategicProfile:
    """Represents a developer's strategic profile for project discovery"""
    # Professional Profile
    current_role: str
    experience_level: str  # junior, mid_level, senior, staff, principal
    primary_technologies: List[str]
    learning_technologies: List[str]
    industry_interests: List[str]
    
    # Career Goals
    target_companies: List[str]
    target_roles: List[str]
    timeline_months: int
    
    # Contribution Preferences
    time_commitment_hours_per_week: int
    preferred_languages: List[str]
    issue_complexity: List[str]  # good-first-issue, help-wanted, documentation, bug, feature
    project_size_preference: str  # startup, established, enterprise

    def __post_init__(self):
        # Ensure all list fields are initialized
        for field_name in ['primary_technologies', 'learning_technologies', 'industry_interests',
                          'target_companies', 'target_roles', 'preferred_languages', 'issue_complexity']:
            field_value = getattr(self, field_name)
            if field_value is None:
                setattr(self, field_name, [])


@dataclass
class ContributionOpportunity:
    """Represents a specific contribution opportunity with strategic context"""
    project: GitHubProject
    opportunity_type: str  # issue, documentation, feature, bug-fix, optimization
    title: str
    description: str
    url: str
    difficulty: str  # beginner, intermediate, advanced
    strategic_value: float  # 0-1 score for career alignment
    learning_value: float   # 0-1 score for skill development
    networking_value: float # 0-1 score for professional connections
    estimated_hours: int
    next_steps: List[str]

    def __post_init__(self):
        if self.next_steps is None:
            self.next_steps = []

    @property
    def total_value_score(self) -> float:
        """Calculate total opportunity value weighted across dimensions"""
        return (self.strategic_value * 0.4 + 
                self.learning_value * 0.3 + 
                self.networking_value * 0.3)


@dataclass
class DiscoveryResult:
    """Container for a complete strategic discovery result"""
    profile: StrategicProfile
    discovered_projects: List[GitHubProject]
    opportunities: List[ContributionOpportunity]
    discovery_timestamp: datetime
    search_parameters: dict

    def get_top_opportunities(self, limit: int = 5) -> List[ContributionOpportunity]:
        """Get top opportunities sorted by total value score"""
        return sorted(self.opportunities, 
                     key=lambda x: x.total_value_score, 
                     reverse=True)[:limit]

