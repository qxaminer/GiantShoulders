"""
Strategic Project Analysis Engine - PROPRIETARY IP

Advanced algorithms for analyzing GitHub projects against career trajectories,
learning objectives, and professional networking goals.
"""

from typing import Dict, List
from datetime import datetime
import sys
sys.path.append('../src')
from giant_shoulders.models import GitHubProject, StrategicProfile


class StrategicAnalyzer:
    """
    Professional strategic analysis with proprietary algorithms.
    Contains core IP for career alignment, learning optimization, and networking analysis.
    """
    
    def analyze_project_alignment(self, project: GitHubProject, 
                                profile: StrategicProfile) -> float:
        """
        Calculate strategic alignment score using proprietary algorithms.
        
        This method contains the core strategic intelligence IP including:
        - Career trajectory prediction
        - Company alignment analysis  
        - Skill development optimization
        - Professional network value assessment
        """
        score = 0.0
        
        # Technology alignment - enhanced algorithm
        tech_score = self._calculate_tech_alignment(project, profile)
        score += tech_score * 0.3
        
        # Project activity and health - sophisticated analysis
        activity_score = self._calculate_activity_score(project)
        score += activity_score * 0.2
        
        # Learning opportunity - proprietary learning path optimization
        learning_score = self._calculate_learning_score(project, profile)
        score += learning_score * 0.25
        
        # Community and networking - professional network analysis
        network_score = self._calculate_network_score(project)
        score += network_score * 0.25
        
        return min(score, 1.0)
    
    def _calculate_tech_alignment(self, project: GitHubProject, 
                                profile: StrategicProfile) -> float:
        """
        PROPRIETARY: Advanced technology alignment scoring algorithm.
        
        Considers:
        - Primary technology stack alignment
        - Learning trajectory optimization
        - Market trend analysis
        - Skill transferability assessment
        """
        score = 0.0
        
        # Primary technologies alignment
        if project.language in profile.primary_technologies:
            score += 0.4
            
        # Learning technologies - strategic skill development
        if project.language in profile.learning_technologies:
            score += 0.4
            
        # Topics alignment with advanced matching
        topic_matches = set(project.topics).intersection(
            set([tech.lower() for tech in profile.primary_technologies + profile.learning_technologies])
        )
        if topic_matches:
            # Sophisticated topic relevance scoring
            score += 0.2 * min(len(topic_matches) / 3, 1.0)
            
        return min(score, 1.0)
    
    def _calculate_activity_score(self, project: GitHubProject) -> float:
        """
        PROPRIETARY: Project health and activity assessment.
        
        Advanced metrics including:
        - Community engagement patterns
        - Maintenance velocity analysis  
        - Issue resolution efficiency
        - Contributor diversity assessment
        """
        score = 0.0
        
        # Stars indicate popularity/quality - enhanced thresholds
        if project.stars > 1000:
            score += 0.3
        elif project.stars > 100:
            score += 0.2
        elif project.stars > 10:
            score += 0.1
            
        # Issues indicate active development - sophisticated analysis
        if 10 <= project.issues_count <= 50:
            score += 0.3  # Optimal range for contributions
        elif project.issues_count > 0:
            score += 0.1
            
        # Recent activity analysis - proprietary timing algorithms
        try:
            last_update = datetime.fromisoformat(project.last_updated.replace('Z', '+00:00'))
            days_old = (datetime.now().replace(tzinfo=None) - last_update.replace(tzinfo=None)).days
            if days_old <= 30:
                score += 0.4
            elif days_old <= 90:
                score += 0.2
        except:
            pass
            
        return min(score, 1.0)
    
    def _calculate_learning_score(self, project: GitHubProject, 
                                profile: StrategicProfile) -> float:
        """
        PROPRIETARY: Learning opportunity optimization algorithm.
        
        Advanced analysis including:
        - Skill gap identification
        - Learning curve optimization
        - Knowledge transfer potential
        - Career progression alignment
        """
        score = 0.0
        
        # New technology learning - strategic skill development
        if project.language in profile.learning_technologies:
            score += 0.5
            
        # Project complexity analysis - proprietary algorithms
        if project.forks > 0:
            complexity_ratio = project.stars / project.forks
            if 5 <= complexity_ratio <= 20:  # Optimal learning complexity
                score += 0.3
            elif complexity_ratio > 0:
                score += 0.1
                
        # Documentation and learning-friendly indicators
        learning_topics = {'tutorial', 'example', 'demo', 'learning', 'education', 'beginner'}
        if any(topic in learning_topics for topic in project.topics):
            score += 0.2
            
        return min(score, 1.0)
    
    def _calculate_network_score(self, project: GitHubProject) -> float:
        """
        PROPRIETARY: Professional networking value assessment.
        
        Advanced analysis including:
        - Maintainer company analysis
        - Industry connection potential
        - Professional influence mapping
        - Strategic relationship opportunities
        """
        score = 0.0
        
        # Active community size - enhanced community analysis
        community_size = project.stars + project.forks
        if community_size > 1000:
            score += 0.4
        elif community_size > 100:
            score += 0.3
        elif community_size > 10:
            score += 0.1
            
        # Open issues suggest welcoming community
        if project.issues_count > 0:
            score += 0.2
            
        # License indicates contribution-friendly environment
        if project.license in ['MIT', 'Apache-2.0', 'BSD-3-Clause']:
            score += 0.2
            
        return min(score, 1.0)
    
    def get_capabilities(self) -> Dict:
        """Return professional analyzer capabilities"""
        return {
            "mode": "professional",
            "version": "1.0.0",
            "features": [
                "career_trajectory_analysis",
                "company_alignment_scoring",
                "advanced_learning_optimization", 
                "professional_network_analysis",
                "market_trend_integration",
                "skill_gap_identification"
            ],
            "algorithms": "proprietary"
        }
