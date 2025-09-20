"""
Giant Shoulders - Strategic Open Source Discovery
Streamlit Web Application
"""

import sys
import os
from pathlib import Path
import streamlit as st
from datetime import datetime
from typing import List

# Add src to Python path
sys.path.append(str(Path(__file__).parent / "src"))

from src.giant_shoulders import (
    StrategicProfile, 
    GitHubStrategicScanner, 
    StrategicAnalyzer, 
    ContributionFinder,
    DiscoveryResult
)

# Page configuration
st.set_page_config(
    page_title="Giant Shoulders - Strategic Open Source Discovery",
    page_icon="🏔️",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    # Header
    st.title("🏔️ Giant Shoulders")
    st.subheader("Strategic Open Source Discovery")
    st.markdown("*Standing on the shoulders of giants - Find GitHub projects aligned with your career goals*")
    
    # Sidebar for profile input
    with st.sidebar:
        st.header("👤 Your Strategic Profile")
        
        # Professional Profile
        st.subheader("Professional Background")
        current_role = st.text_input("Current Role", placeholder="e.g., Software Engineer")
        
        experience_level = st.selectbox(
            "Experience Level",
            ["junior", "mid_level", "senior", "staff", "principal"]
        )
        
        # Technologies
        st.subheader("Technologies")
        primary_tech = st.text_area(
            "Primary Technologies (comma-separated)", 
            placeholder="Python, JavaScript, React"
        ).split(",") if st.text_area(
            "Primary Technologies (comma-separated)", 
            placeholder="Python, JavaScript, React"
        ) else []
        
        learning_tech = st.text_area(
            "Learning Technologies (comma-separated)",
            placeholder="Go, Rust, Machine Learning"
        ).split(",") if st.text_area(
            "Learning Technologies (comma-separated)",
            placeholder="Go, Rust, Machine Learning"
        ) else []
        
        # Clean up technology lists
        primary_tech = [tech.strip() for tech in primary_tech if tech.strip()]
        learning_tech = [tech.strip() for tech in learning_tech if tech.strip()]
        
        # Career Goals
        st.subheader("Career Goals")
        target_companies = st.text_area(
            "Target Companies (comma-separated)",
            placeholder="Google, Microsoft, Stripe"
        ).split(",") if st.text_area(
            "Target Companies (comma-separated)",
            placeholder="Google, Microsoft, Stripe"
        ) else []
        target_companies = [comp.strip() for comp in target_companies if comp.strip()]
        
        target_roles = st.text_area(
            "Target Roles (comma-separated)",
            placeholder="Senior Engineer, Tech Lead, Principal Engineer"
        ).split(",") if st.text_area(
            "Target Roles (comma-separated)",
            placeholder="Senior Engineer, Tech Lead, Principal Engineer"
        ) else []
        target_roles = [role.strip() for role in target_roles if role.strip()]
        
        timeline_months = st.slider("Career Timeline (months)", 3, 36, 12)
        
        # Contribution Preferences
        st.subheader("Contribution Preferences")
        time_commitment = st.slider("Hours per week", 1, 20, 5)
        
        issue_complexity = st.multiselect(
            "Preferred Issue Types",
            ["good-first-issue", "help-wanted", "documentation", "bug", "feature"],
            default=["good-first-issue", "documentation"]
        )
        
        project_size = st.selectbox(
            "Project Size Preference",
            ["startup", "established", "enterprise"]
        )
        
        # Industry interests
        industry_interests = st.text_area(
            "Industry Interests (comma-separated)",
            placeholder="fintech, healthcare, education"
        ).split(",") if st.text_area(
            "Industry Interests (comma-separated)",
            placeholder="fintech, healthcare, education"
        ) else []
        industry_interests = [interest.strip() for interest in industry_interests if interest.strip()]
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Search parameters
        st.header("🔍 Discovery Parameters")
        
        search_query = st.text_input(
            "Search Query", 
            placeholder="e.g., web framework, machine learning, data visualization",
            value="web framework"
        )
        
        preferred_language = st.selectbox(
            "Preferred Programming Language (optional)",
            ["Any"] + ["Python", "JavaScript", "TypeScript", "Go", "Rust", "Java", "C++", "Ruby"],
            index=0
        )
        
        min_stars = st.number_input("Minimum Stars", min_value=0, value=100)
        max_results = st.slider("Maximum Results", 5, 50, 15)
        
        # Discovery button
        if st.button("🚀 Discover Strategic Projects", type="primary"):
            if not current_role or not search_query:
                st.error("Please fill in at least your current role and search query.")
            else:
                discover_projects(
                    current_role=current_role,
                    experience_level=experience_level,
                    primary_tech=primary_tech,
                    learning_tech=learning_tech,
                    target_companies=target_companies,
                    target_roles=target_roles,
                    timeline_months=timeline_months,
                    time_commitment=time_commitment,
                    issue_complexity=issue_complexity,
                    project_size=project_size,
                    industry_interests=industry_interests,
                    search_query=search_query,
                    preferred_language=preferred_language if preferred_language != "Any" else None,
                    min_stars=min_stars,
                    max_results=max_results
                )
    
    with col2:
        # Info panel
        st.header("ℹ️ How It Works")
        st.markdown("""
        **Giant Shoulders** analyzes GitHub projects against your career goals to find strategic contribution opportunities.
        
        **Discovery Process:**
        1. **Profile Analysis** - We analyze your career trajectory and goals
        2. **Strategic Search** - Find projects aligned with your objectives  
        3. **Opportunity Mapping** - Identify specific contribution opportunities
        4. **Strategic Scoring** - Rate opportunities by career impact
        
        **Strategic Factors:**
        - 🎯 **Career Alignment** - How well does this advance your goals?
        - 📈 **Learning Value** - What new skills will you develop?
        - 🤝 **Networking** - Connect with relevant industry professionals
        - ⚡ **Impact** - Make meaningful contributions that matter
        """)


def discover_projects(current_role: str, experience_level: str, primary_tech: List[str],
                     learning_tech: List[str], target_companies: List[str], target_roles: List[str],
                     timeline_months: int, time_commitment: int, issue_complexity: List[str],
                     project_size: str, industry_interests: List[str], search_query: str,
                     preferred_language: str = None, min_stars: int = 100, max_results: int = 15):
    """Execute the strategic discovery process"""
    
    # Create strategic profile
    profile = StrategicProfile(
        current_role=current_role,
        experience_level=experience_level,
        primary_technologies=primary_tech,
        learning_technologies=learning_tech,
        industry_interests=industry_interests,
        target_companies=target_companies,
        target_roles=target_roles,
        timeline_months=timeline_months,
        time_commitment_hours_per_week=time_commitment,
        preferred_languages=[preferred_language] if preferred_language else [],
        issue_complexity=issue_complexity,
        project_size_preference=project_size
    )
    
    # Initialize discovery components
    with st.spinner("🔍 Scanning GitHub ecosystem..."):
        scanner = GitHubStrategicScanner()
        analyzer = StrategicAnalyzer()
        finder = ContributionFinder()
        
        # Search for projects
        projects = scanner.search_repositories(
            query=search_query,
            language=preferred_language,
            min_stars=min_stars,
            max_results=max_results
        )
        
        if not projects:
            st.error("No projects found matching your criteria. Try adjusting your search parameters.")
            return
        
        # Analyze strategic alignment
        st.write(f"📊 Analyzing {len(projects)} projects for strategic alignment...")
        progress_bar = st.progress(0)
        
        for i, project in enumerate(projects):
            strategic_score = analyzer.analyze_project_alignment(project, profile)
            project.strategic_score = strategic_score
            progress_bar.progress((i + 1) / len(projects))
        
        # Sort by strategic score
        projects.sort(key=lambda x: x.strategic_score or 0, reverse=True)
        
        # Find contribution opportunities
        opportunities = finder.find_opportunities(projects[:10], profile)  # Top 10 for opportunities
        
    # Display results
    st.success(f"✅ Discovery complete! Found {len(projects)} strategic projects")
    
    # Results tabs
    tab1, tab2, tab3 = st.tabs(["🎯 Strategic Projects", "🛠️ Contribution Opportunities", "📊 Analysis"])
    
    with tab1:
        display_strategic_projects(projects[:10])  # Top 10
    
    with tab2:
        display_contribution_opportunities(opportunities)
    
    with tab3:
        display_strategic_analysis(projects, profile)


def display_strategic_projects(projects):
    """Display strategic projects with scoring"""
    st.header("🎯 Strategic Projects Ranked by Career Alignment")
    
    for i, project in enumerate(projects, 1):
        with st.expander(f"#{i} {project.name} by {project.owner} ⭐ {project.stars}"):
            col1, col2 = st.columns([3, 1])
            
            with col1:
                st.markdown(f"**Description:** {project.description}")
                st.markdown(f"**Language:** {project.language}")
                st.markdown(f"**Topics:** {', '.join(project.topics) if project.topics else 'None'}")
                st.markdown(f"**License:** {project.license or 'Unknown'}")
                st.markdown(f"🔗 **[View on GitHub]({project.url})**")
            
            with col2:
                # Strategic score display
                score = project.strategic_score or 0
                st.metric("Strategic Score", f"{score:.1%}")
                
                # Project stats
                st.write(f"⭐ {project.stars:,} stars")
                st.write(f"🔀 {project.forks:,} forks") 
                st.write(f"🐛 {project.issues_count} open issues")


def display_contribution_opportunities(opportunities):
    """Display specific contribution opportunities"""
    st.header("🛠️ Strategic Contribution Opportunities")
    
    if not opportunities:
        st.info("No specific contribution opportunities found. Try adjusting your search parameters.")
        return
    
    # Sort by total value score
    sorted_opportunities = sorted(opportunities, key=lambda x: x.total_value_score, reverse=True)
    
    for i, opp in enumerate(sorted_opportunities[:10], 1):  # Top 10
        with st.expander(f"#{i} {opp.title} - {opp.project.name} ({opp.difficulty})"):
            col1, col2 = st.columns([2, 1])
            
            with col1:
                st.markdown(f"**Project:** {opp.project.name} by {opp.project.owner}")
                st.markdown(f"**Opportunity:** {opp.description}")
                st.markdown(f"**Type:** {opp.opportunity_type}")
                st.markdown(f"**Estimated Time:** {opp.estimated_hours} hours")
                
                st.markdown("**Next Steps:**")
                for step in opp.next_steps:
                    st.markdown(f"- {step}")
                
                st.markdown(f"🔗 **[View Opportunity]({opp.url})**")
            
            with col2:
                st.metric("Strategic Value", f"{opp.strategic_value:.1%}")
                st.metric("Learning Value", f"{opp.learning_value:.1%}")
                st.metric("Networking Value", f"{opp.networking_value:.1%}")
                st.metric("Total Score", f"{opp.total_value_score:.1%}")


def display_strategic_analysis(projects, profile):
    """Display strategic analysis and insights"""
    st.header("📊 Strategic Analysis")
    
    # Summary metrics
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        avg_score = sum(p.strategic_score or 0 for p in projects) / len(projects)
        st.metric("Avg Strategic Score", f"{avg_score:.1%}")
    
    with col2:
        languages = [p.language for p in projects if p.language]
        top_language = max(set(languages), key=languages.count) if languages else "Unknown"
        st.metric("Top Language", top_language)
    
    with col3:
        total_stars = sum(p.stars for p in projects)
        st.metric("Total Stars", f"{total_stars:,}")
    
    with col4:
        avg_issues = sum(p.issues_count for p in projects) / len(projects)
        st.metric("Avg Open Issues", f"{avg_issues:.1f}")
    
    # Strategic insights
    st.subheader("🔍 Strategic Insights")
    
    high_value_projects = [p for p in projects if (p.strategic_score or 0) > 0.7]
    if high_value_projects:
        st.success(f"🎯 Found {len(high_value_projects)} high-value strategic projects (>70% alignment)")
    
    learning_opportunities = [p for p in projects if p.language in profile.learning_technologies]
    if learning_opportunities:
        st.info(f"📚 {len(learning_opportunities)} projects match your learning technologies")
    
    recent_projects = [p for p in projects 
                      if (datetime.now() - datetime.fromisoformat(p.last_updated.replace('Z', '+00:00')).replace(tzinfo=None)).days <= 30]
    if recent_projects:
        st.info(f"🚀 {len(recent_projects)} projects were updated in the last 30 days")


if __name__ == "__main__":
    main()
