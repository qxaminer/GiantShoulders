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


# StrategicAnalyzer and ContributionFinder classes moved to gs_core module
# for IP protection. They are now imported via the flexible import system in app.py

