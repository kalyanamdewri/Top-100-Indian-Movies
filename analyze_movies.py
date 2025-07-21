#!/usr/bin/env python3
"""
Top 100 Indian Movies Analysis
Data analysis script for Indian cinema ratings and statistics
"""

import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import numpy as np

def load_movie_data():
    """Load the movie data from JSON file"""
    with open('data/top_100_indian_movies.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def analyze_movies(movies):
    """Perform comprehensive analysis of the movie data"""
    df = pd.DataFrame(movies)
    
    print("=== TOP 100 INDIAN MOVIES ANALYSIS ===")
    print(f"Total movies analyzed: {len(df)}")
    print(f"Year range: {df['year'].min()} - {df['year'].max()}")
    print(f"Rating range: {df['rating'].min()} - {df['rating'].max()}")
    print(f"Vote range: {df['votes'].min():,} - {df['votes'].max():,}")
    print()
    
    # Year distribution analysis
    print("=== YEAR DISTRIBUTION ===")
    year_counts = df['year'].value_counts().sort_index()
    print("Movies by decade:")
    decades = {}
    for year in df['year']:
        decade = (year // 10) * 10
        decades[decade] = decades.get(decade, 0) + 1
    
    for decade in sorted(decades.keys()):
        print(f"{decade}s: {decades[decade]} movies")
    print()
    
    # Rating distribution analysis
    print("=== RATING DISTRIBUTION ===")
    rating_ranges = {
        '9.0+': len(df[df['rating'] >= 9.0]),
        '8.5-8.9': len(df[(df['rating'] >= 8.5) & (df['rating'] < 9.0)]),
        '8.0-8.4': len(df[(df['rating'] >= 8.0) & (df['rating'] < 8.5)]),
        '7.8-7.9': len(df[(df['rating'] >= 7.8) & (df['rating'] < 8.0)])
    }
    
    for range_name, count in rating_ranges.items():
        print(f"{range_name}: {count} movies")
    print()
    
    # Vote distribution analysis
    print("=== VOTE DISTRIBUTION ===")
    vote_ranges = {
        '500K+': len(df[df['votes'] >= 500000]),
        '100K-499K': len(df[(df['votes'] >= 100000) & (df['votes'] < 500000)]),
        '50K-99K': len(df[(df['votes'] >= 50000) & (df['votes'] < 100000)]),
        '10K-49K': len(df[(df['votes'] >= 10000) & (df['votes'] < 50000)])
    }
    
    for range_name, count in vote_ranges.items():
        print(f"{range_name}: {count} movies")
    print()
    
    # Top movies by different criteria
    print("=== TOP 10 BY RATING ===")
    top_by_rating = df.nlargest(10, 'rating')
    for _, movie in top_by_rating.iterrows():
        print(f"{movie['rank']}. {movie['title']} ({movie['year']}) - {movie['rating']}/10")
    print()
    
    print("=== TOP 10 BY VOTES ===")
    top_by_votes = df.nlargest(10, 'votes')
    for _, movie in top_by_votes.iterrows():
        print(f"{movie['rank']}. {movie['title']} ({movie['year']}) - {movie['votes']:,} votes")
    print()
    
    print("=== MOST RECENT MOVIES (2020+) ===")
    recent_movies = df[df['year'] >= 2020].sort_values('rating', ascending=False)
    for _, movie in recent_movies.head(10).iterrows():
        print(f"{movie['rank']}. {movie['title']} ({movie['year']}) - {movie['rating']}/10")
    print()
    
    return df

def create_visualizations(df):
    """Create visualizations for the movie data"""
    plt.style.use('default')
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Top 100 Indian Movies Analysis (2000+)', fontsize=16, fontweight='bold')
    
    # 1. Movies by decade
    decades = {}
    for year in df['year']:
        decade = (year // 10) * 10
        decades[decade] = decades.get(decade, 0) + 1
    
    decade_labels = [f"{d}s" for d in sorted(decades.keys())]
    decade_counts = [decades[d] for d in sorted(decades.keys())]
    
    axes[0, 0].bar(decade_labels, decade_counts, color='skyblue', edgecolor='navy')
    axes[0, 0].set_title('Movies by Decade')
    axes[0, 0].set_ylabel('Number of Movies')
    axes[0, 0].grid(axis='y', alpha=0.3)
    
    # 2. Rating distribution
    axes[0, 1].hist(df['rating'], bins=15, color='lightgreen', edgecolor='darkgreen', alpha=0.7)
    axes[0, 1].set_title('Rating Distribution')
    axes[0, 1].set_xlabel('IMDb Rating')
    axes[0, 1].set_ylabel('Number of Movies')
    axes[0, 1].grid(axis='y', alpha=0.3)
    
    # 3. Votes vs Rating scatter plot
    scatter = axes[1, 0].scatter(df['votes'], df['rating'], alpha=0.6, c=df['year'], cmap='viridis')
    axes[1, 0].set_title('Votes vs Rating (colored by year)')
    axes[1, 0].set_xlabel('Number of Votes')
    axes[1, 0].set_ylabel('IMDb Rating')
    axes[1, 0].set_xscale('log')
    axes[1, 0].grid(alpha=0.3)
    plt.colorbar(scatter, ax=axes[1, 0], label='Year')
    
    # 4. Top 15 movies by rating
    top_15 = df.nlargest(15, 'rating')
    y_pos = np.arange(len(top_15))
    axes[1, 1].barh(y_pos, top_15['rating'], color='coral')
    axes[1, 1].set_yticks(y_pos)
    axes[1, 1].set_yticklabels([f"{movie['title'][:20]}..." if len(movie['title']) > 20 else movie['title'] 
                               for _, movie in top_15.iterrows()], fontsize=8)
    axes[1, 1].set_title('Top 15 Movies by Rating')
    axes[1, 1].set_xlabel('IMDb Rating')
    axes[1, 1].grid(axis='x', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('visualizations/movie_analysis_charts.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    # Create a timeline chart
    plt.figure(figsize=(15, 8))
    
    # Group movies by year and calculate average rating
    yearly_stats = df.groupby('year').agg({
        'rating': ['mean', 'count'],
        'votes': 'mean'
    }).round(2)
    
    yearly_stats.columns = ['avg_rating', 'movie_count', 'avg_votes']
    yearly_stats = yearly_stats.reset_index()
    
    # Create subplot for timeline
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))
    
    # Timeline of movies
    ax1.scatter(df['year'], df['rating'], s=df['votes']/1000, alpha=0.6, c=df['rating'], cmap='RdYlGn')
    ax1.set_title('Timeline of Top 100 Indian Movies (2000+)\nBubble size = Number of votes, Color = Rating')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('IMDb Rating')
    ax1.grid(alpha=0.3)
    ax1.set_ylim(7.7, 9.1)
    
    # Add colorbar
    sm = plt.cm.ScalarMappable(cmap='RdYlGn', norm=plt.Normalize(vmin=df['rating'].min(), vmax=df['rating'].max()))
    sm.set_array([])
    plt.colorbar(sm, ax=ax1, label='IMDb Rating')
    
    # Movies per year
    year_counts = df['year'].value_counts().sort_index()
    ax2.bar(year_counts.index, year_counts.values, alpha=0.7, color='steelblue')
    ax2.set_title('Number of Top Movies by Year')
    ax2.set_xlabel('Year')
    ax2.set_ylabel('Number of Movies')
    ax2.grid(axis='y', alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('visualizations/movie_timeline.png', dpi=300, bbox_inches='tight')
    plt.close()
    
    print("Visualizations saved:")
    print("- visualizations/movie_analysis_charts.png")
    print("- visualizations/movie_timeline.png")

def generate_summary_stats(df):
    """Generate summary statistics"""
    stats = {
        'total_movies': int(len(df)),
        'avg_rating': float(round(df['rating'].mean(), 2)),
        'median_rating': float(round(df['rating'].median(), 2)),
        'avg_votes': int(df['votes'].mean()),
        'median_votes': int(df['votes'].median()),
        'year_range': f"{int(df['year'].min())}-{int(df['year'].max())}",
        'most_productive_year': int(df['year'].value_counts().index[0]),
        'highest_rated_movie': str(df.loc[df['rating'].idxmax()]['title']),
        'most_voted_movie': str(df.loc[df['votes'].idxmax()]['title']),
        'newest_movie': str(df.loc[df['year'].idxmax()]['title']),
        'oldest_movie': str(df.loc[df['year'].idxmin()]['title'])
    }
    
    return stats

if __name__ == "__main__":
    # Load and analyze data
    movies = load_movie_data()
    df = analyze_movies(movies)
    
    # Create visualizations
    create_visualizations(df)
    
    # Generate summary statistics
    stats = generate_summary_stats(df)
    
    # Save summary statistics
    with open('data/movie_summary_stats.json', 'w', encoding='utf-8') as f:
        json.dump(stats, f, indent=2, ensure_ascii=False)
    
    print("\nSUMMARY STATISTICS:")
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    
    print("\nAnalysis complete! Files generated:")
    print("- data/top_100_indian_movies.json")
    print("- visualizations/movie_analysis_charts.png") 
    print("- visualizations/movie_timeline.png")
    print("- data/movie_summary_stats.json")

