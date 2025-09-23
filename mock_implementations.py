"""
Mock implementations for public Giant Shoulders demo.

These simplified implementations demonstrate the concept and user experience
without revealing the proprietary strategic analysis algorithms.
"""

import random
from typing import List, Dict
from datetime import datetime
import sys
sys.path.append('src')
from giant_shoulders.models import GitHubProject, StrategicProfile, ContributionOpportunity


class MockStrategicAnalyzer:
    """
    Simplified analyzer for public demonstration.
    
    Shows the interface and basic functionality without proprietary algorithms.
    """
    
    def analyze_project_alignment(self, project: GitHubProject, 
                                 profile: StrategicProfile) -> float:
        """
        Basic alignment scoring for demo purposes.
        Real strategic analysis available in professional version.
        """
        score = 0.0
        
        # Simple language matching
        if project.language in profile.primary_technologies:
            score += 0.5
        if project.language in profile.learning_technologies:
            score += 0.3
            
        # Star-based quality indicator  
        if project.stars > 1000:
            score += 0.2
        elif project.stars > 100:
            score += 0.1
            
        # Add some randomness to make demo interesting
        score += random.uniform(-0.1, 0.1)
            
        return max(0.0, min(score, 1.0))
    
    def get_capabilities(self) -> Dict:
        """Return demo analyzer capabilities and limitations"""
        return {
            "mode": "demo",
            "version": "public-demo-1.0",
            "features": [
                "basic_language_matching", 
                "star_popularity_scoring",
                "simple_project_filtering"
            ],
            "limitations": [
                "No career trajectory analysis",
                "No company alignment scoring", 
                "No advanced learning path optimization",
                "No professional networking analysis",
                "No market trend integration",
                "No strategic timing analysis"
            ],
            "upgrade_info": {
                "message": "Professional strategic analysis available separately",
                "features": [
                    "🎯 Career trajectory optimization",
                    "🏢 Target company alignment analysis", 
                    "📈 Advanced learning path planning",
                    "🤝 Professional networking value assessment",
                    "📊 Market timing and trend analysis",
                    "🧠 AI-powered strategic recommendations"
                ]
            }
        }


class MockContributionFinder:
    """
    Demo contribution opportunity finder.
    
    Generates realistic sample opportunities to demonstrate the concept.
    """
    
    def find_opportunities(self, projects: List[GitHubProject],
                         profile: StrategicProfile) -> List[ContributionOpportunity]:
        """Generate sample opportunities for demonstration"""
        opportunities = []
        
        # Limit to top projects for demo
        demo_projects = projects[:5]
        
        for project in demo_projects:
            # Create 1-2 opportunities per project
            num_opportunities = random.randint(1, 2)
            
            for i in range(num_opportunities):
                opp = self._create_demo_opportunity(project, profile)
                if opp:
                    opportunities.append(opp)
        
        # Sort by total value score
        opportunities.sort(key=lambda x: x.total_value_score, reverse=True)
        
        return opportunities[:10]  # Return top 10 for demo
    
    def _create_demo_opportunity(self, project: GitHubProject,
                               profile: StrategicProfile) -> ContributionOpportunity:
        """Create a realistic demo opportunity"""
        
        # Random opportunity type
        opp_types = [
            ("documentation", "Documentation Enhancement", "beginner", 3, 6),
            ("bug", "Bug Fix Contribution", "intermediate", 4, 12), 
            ("feature", "Feature Implementation", "intermediate", 8, 20),
            ("testing", "Test Coverage Improvement", "beginner", 2, 8)
        ]
        
        opp_type, title_template, difficulty, min_hours, max_hours = random.choice(opp_types)
        
        # Simple scoring - no proprietary algorithms
        strategic_value = random.uniform(0.4, 0.8)
        learning_value = random.uniform(0.3, 0.9)
        networking_value = random.uniform(0.2, 0.7)
        
        # Boost scores if languages match
        if project.language in profile.primary_technologies:
            strategic_value = min(1.0, strategic_value + 0.1)
            learning_value = min(1.0, learning_value + 0.1)
        
        if project.language in profile.learning_technologies:
            learning_value = min(1.0, learning_value + 0.2)
        
        # Generate description
        descriptions = {
            "documentation": f"Improve the getting started guide and API documentation for {project.name}",
            "bug": f"Fix identified issues in {project.name} to improve stability and user experience", 
            "feature": f"Implement new functionality for {project.name} based on community requests",
            "testing": f"Enhance test coverage and quality assurance for {project.name}"
        }
        
        # Generate next steps
        next_steps_templates = {
            "documentation": [
                "Review existing documentation structure",
                "Identify gaps and improvement opportunities",
                "Draft enhanced documentation sections",
                "Collaborate with maintainers on content review",
                "Submit documentation improvements"
            ],
            "bug": [
                "Analyze reported issues and reproduction steps",
                "Study codebase to understand the problem area", 
                "Develop and test potential fixes",
                "Write or update relevant tests",
                "Submit pull request with fix and tests"
            ],
            "feature": [
                "Research feature requirements and use cases",
                "Design implementation approach",
                "Discuss approach with project maintainers",
                "Implement feature with comprehensive tests",
                "Submit pull request and iterate based on feedback"
            ],
            "testing": [
                "Analyze current test coverage",
                "Identify critical areas needing test coverage",
                "Write comprehensive test suites", 
                "Ensure tests follow project conventions",
                "Submit testing improvements"
            ]
        }
        
        return ContributionOpportunity(
            project=project,
            opportunity_type=opp_type,
            title=f"{title_template} - {project.name}",
            description=descriptions[opp_type],
            url=f"{project.url}/issues",
            difficulty=difficulty,
            strategic_value=strategic_value,
            learning_value=learning_value,
            networking_value=networking_value,
            estimated_hours=random.randint(min_hours, max_hours),
            next_steps=next_steps_templates[opp_type]
        )
    
    def get_capabilities(self) -> Dict:
        """Return demo finder capabilities"""
        return {
            "mode": "demo",
            "version": "public-demo-1.0",
            "features": [
                "basic_opportunity_generation",
                "simple_scoring_algorithms", 
                "opportunity_type_variety"
            ],
            "limitations": [
                "No real GitHub issue analysis",
                "No strategic career value optimization",
                "No advanced timing analysis",
                "No maintainer background research",
                "No professional networking optimization",
                "Limited opportunity types"
            ],
            "upgrade_info": {
                "message": "Professional opportunity analysis available separately",
                "features": [
                    "🔍 Real GitHub issue analysis and matching",
                    "🎯 Strategic career value optimization",
                    "⏰ Optimal timing analysis",
                    "👥 Maintainer and community research",
                    "🤝 Professional networking opportunities",
                    "📊 Advanced opportunity ranking algorithms"
                ]
            }
        }
