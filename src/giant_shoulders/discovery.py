"""
Strategic GitHub project discovery engine for Giant Shoulders.
"""

import random
import requests
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from .models import GitHubProject, StrategicProfile, ContributionOpportunity, DiscoveryResult


class GitHubStrategicScanner:
    """
    Scans GitHub for projects aligned with strategic criteria.
    Demo implementation using GitHub API.
    """
    
    def __init__(self, github_token: Optional[str] = None):
        self.github_token = github_token
        self.base_url = "https://api.github.com"
        self.headers = {
            'Accept': 'application/vnd.github.v3+json',
            'User-Agent': 'Giant-Shoulders-Discovery-Bot'
        }
        if github_token:
            self.headers['Authorization'] = f'token {github_token}'
    
    def search_repositories(self, query: str, language: str = None, 
                          min_stars: int = 10, max_results: int = 20) -> List[GitHubProject]:
        """Search GitHub repositories based on criteria"""
        
        # Build search query
        search_parts = [query]
        if language:
            search_parts.append(f'language:{language}')
        search_parts.append(f'stars:>={min_stars}')
        search_parts.append('fork:false')  # Exclude forks
        
        search_query = ' '.join(search_parts)
        
        params = {
            'q': search_query,
            'sort': 'stars',
            'order': 'desc',
            'per_page': min(max_results, 100)
        }
        
        try:
            response = requests.get(
                f"{self.base_url}/search/repositories",
                headers=self.headers,
                params=params,
                timeout=10
            )
            response.raise_for_status()
            
            data = response.json()
            projects = []
            
            for repo in data.get('items', []):
                project = GitHubProject(
                    name=repo['name'],
                    owner=repo['owner']['login'],
                    description=repo.get('description', ''),
                    url=repo['html_url'],
                    language=repo.get('language', 'Unknown'),
                    stars=repo['stargazers_count'],
                    forks=repo['forks_count'],
                    issues_count=repo['open_issues_count'],
                    last_updated=repo['updated_at'],
                    topics=repo.get('topics', []),
                    license=repo.get('license', {}).get('name') if repo.get('license') else None
                )
                projects.append(project)
            
            return projects
            
        except requests.RequestException as e:
            print(f"Error searching repositories: {e}")
            return self._get_demo_projects(query, language)
    
    def _get_demo_projects(self, query: str, language: str = None) -> List[GitHubProject]:
        """Generate demo projects when API is unavailable"""
        demo_projects = [
            GitHubProject(
                name=f"awesome-{query.lower().replace(' ', '-')}",
                owner="demo-org",
                description=f"A curated list of awesome {query} resources and tools",
                url=f"https://github.com/demo-org/awesome-{query.lower().replace(' ', '-')}",
                language=language or "Python",
                stars=random.randint(500, 5000),
                forks=random.randint(50, 500),
                issues_count=random.randint(10, 100),
                last_updated=(datetime.now() - timedelta(days=random.randint(1, 30))).isoformat(),
                topics=[query.lower(), "awesome-list", "resources"],
                license="MIT"
            ),
            GitHubProject(
                name=f"{query.lower().replace(' ', '-')}-toolkit",
                owner="contrib-team",
                description=f"Professional toolkit for {query} development with modern best practices",
                url=f"https://github.com/contrib-team/{query.lower().replace(' ', '-')}-toolkit",
                language=language or "TypeScript",
                stars=random.randint(200, 2000),
                forks=random.randint(30, 300),
                issues_count=random.randint(5, 50),
                last_updated=(datetime.now() - timedelta(days=random.randint(1, 15))).isoformat(),
                topics=[query.lower(), "toolkit", "best-practices"],
                license="Apache-2.0"
            ),
            GitHubProject(
                name=f"learn-{query.lower().replace(' ', '-')}",
                owner="education-collective",
                description=f"Interactive learning platform for mastering {query} concepts",
                url=f"https://github.com/education-collective/learn-{query.lower().replace(' ', '-')}",
                language=language or "JavaScript",
                stars=random.randint(100, 1000),
                forks=random.randint(20, 200),
                issues_count=random.randint(15, 75),
                last_updated=(datetime.now() - timedelta(days=random.randint(1, 10))).isoformat(),
                topics=[query.lower(), "education", "interactive", "learning"],
                license="MIT"
            )
        ]
        return demo_projects


class StrategicAnalyzer:
    """
    Analyzes projects for strategic alignment with career goals.
    """
    
    def analyze_project_alignment(self, project: GitHubProject, 
                                profile: StrategicProfile) -> float:
        """Calculate strategic alignment score (0-1)"""
        score = 0.0
        
        # Technology alignment
        tech_score = self._calculate_tech_alignment(project, profile)
        score += tech_score * 0.3
        
        # Project activity and health
        activity_score = self._calculate_activity_score(project)
        score += activity_score * 0.2
        
        # Learning opportunity
        learning_score = self._calculate_learning_score(project, profile)
        score += learning_score * 0.25
        
        # Community and networking
        network_score = self._calculate_network_score(project)
        score += network_score * 0.25
        
        return min(score, 1.0)
    
    def _calculate_tech_alignment(self, project: GitHubProject, 
                                profile: StrategicProfile) -> float:
        """Calculate technology alignment score"""
        score = 0.0
        
        # Primary technologies
        if project.language in profile.primary_technologies:
            score += 0.4
            
        # Learning technologies
        if project.language in profile.learning_technologies:
            score += 0.4
            
        # Topics alignment
        topic_matches = set(project.topics).intersection(
            set([tech.lower() for tech in profile.primary_technologies + profile.learning_technologies])
        )
        if topic_matches:
            score += 0.2 * min(len(topic_matches) / 3, 1.0)
            
        return min(score, 1.0)
    
    def _calculate_activity_score(self, project: GitHubProject) -> float:
        """Calculate project activity and health score"""
        score = 0.0
        
        # Stars indicate popularity/quality
        if project.stars > 1000:
            score += 0.3
        elif project.stars > 100:
            score += 0.2
        elif project.stars > 10:
            score += 0.1
            
        # Issues indicate active development
        if 10 <= project.issues_count <= 50:
            score += 0.3  # Sweet spot
        elif project.issues_count > 0:
            score += 0.1
            
        # Recent activity
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
        """Calculate learning opportunity score"""
        score = 0.0
        
        # New technology learning
        if project.language in profile.learning_technologies:
            score += 0.5
            
        # Project complexity (based on stars/forks ratio)
        if project.forks > 0:
            complexity_ratio = project.stars / project.forks
            if 5 <= complexity_ratio <= 20:  # Good balance
                score += 0.3
            elif complexity_ratio > 0:
                score += 0.1
                
        # Documentation and learning-friendly topics
        learning_topics = {'tutorial', 'example', 'demo', 'learning', 'education', 'beginner'}
        if any(topic in learning_topics for topic in project.topics):
            score += 0.2
            
        return min(score, 1.0)
    
    def _calculate_network_score(self, project: GitHubProject) -> float:
        """Calculate networking opportunity score"""
        score = 0.0
        
        # Active community (stars + forks)
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
            
        # License indicates open contribution
        if project.license in ['MIT', 'Apache-2.0', 'BSD-3-Clause']:
            score += 0.2
            
        return min(score, 1.0)


class ContributionFinder:
    """
    Finds specific contribution opportunities within projects.
    """
    
    def find_opportunities(self, projects: List[GitHubProject], 
                         profile: StrategicProfile) -> List[ContributionOpportunity]:
        """Find contribution opportunities in projects"""
        opportunities = []
        
        for project in projects:
            # Generate demo opportunities for each project
            project_opportunities = self._generate_demo_opportunities(project, profile)
            opportunities.extend(project_opportunities)
            
        return opportunities
    
    def _generate_demo_opportunities(self, project: GitHubProject, 
                                   profile: StrategicProfile) -> List[ContributionOpportunity]:
        """Generate demo contribution opportunities"""
        opportunities = []
        
        # Documentation opportunity
        if random.random() > 0.3:  # 70% chance
            opportunities.append(ContributionOpportunity(
                project=project,
                opportunity_type="documentation",
                title="Improve Getting Started Documentation",
                description=f"Help new contributors understand how to set up and contribute to {project.name}",
                url=f"{project.url}/issues",
                difficulty="beginner",
                strategic_value=0.6,
                learning_value=0.4,
                networking_value=0.7,
                estimated_hours=random.randint(2, 8),
                next_steps=[
                    "Review existing documentation",
                    "Identify gaps in setup instructions", 
                    "Draft improved documentation",
                    "Submit pull request with changes"
                ]
            ))
        
        # Code contribution opportunity
        if random.random() > 0.5:  # 50% chance
            difficulties = ["beginner", "intermediate", "advanced"]
            difficulty = random.choice(difficulties)
            
            opportunities.append(ContributionOpportunity(
                project=project,
                opportunity_type="feature",
                title=f"Implement {project.language} Enhancement",
                description=f"Add new functionality to improve {project.name}'s core capabilities",
                url=f"{project.url}/issues",
                difficulty=difficulty,
                strategic_value=0.8,
                learning_value=0.9,
                networking_value=0.6,
                estimated_hours=random.randint(5, 20),
                next_steps=[
                    "Study existing codebase architecture",
                    "Discuss implementation approach with maintainers",
                    "Create feature branch and implement changes",
                    "Write tests and update documentation",
                    "Submit pull request for review"
                ]
            ))
        
        return opportunities
