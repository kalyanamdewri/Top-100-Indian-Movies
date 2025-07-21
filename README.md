# Top 100 Indian Movies Analysis

A comprehensive data analysis project examining the highest-rated Indian movies from 2000 onwards, based on IMDb ratings and user engagement metrics.

## 🎬 Project Overview

This project analyzes the top 100 Indian movies that meet specific quality and popularity criteria:
- **IMDb Rating:** ≥ 7.8/10
- **User Votes:** ≥ 10,000 votes
- **Release Period:** 2000 onwards
- **Origin:** Indian cinema (all languages and regions)

## 📊 Key Findings

- **100 movies** analyzed spanning 25+ years
- **Average rating:** 8.24/10
- **Most productive decade:** 2010s (47 movies)
- **Highest rated:** The Silence of Swastika (2021) - 9.0/10
- **Most voted:** Slumdog Millionaire (2008) - 898,000 votes

## 🗂️ Project Structure

```
top-100-indian-movies/
├── data/
│   ├── top_100_indian_movies.json      # Complete dataset
│   └── movie_summary_stats.json        # Statistical summary
├── visualizations/
│   ├── movie_analysis_charts.png       # Analysis charts
│   └── movie_timeline.png              # Timeline visualization
├── reports/
│   ├── README.md                       # Detailed analysis report
│   └── Top_100_Indian_Movies_Report.xlsx # Excel report
├── analyze_movies.py                   # Main analysis script
├── generate_report.py                  # Report generation script
└── README.md                          # This file
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas matplotlib seaborn openpyxl numpy
```

### Running the Analysis

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd top-100-indian-movies
   ```

2. **Run the analysis:**
   ```bash
   python analyze_movies.py
   ```

3. **Generate reports:**
   ```bash
   python generate_report.py
   ```

## 📈 Analysis Features

### Statistical Analysis
- Distribution by decade and year
- Rating and vote count analysis
- Temporal trends and patterns
- Top performers by various metrics

### Visualizations
- **Decade Distribution:** Movies by time period
- **Rating Distribution:** Quality metrics spread
- **Timeline Analysis:** Chronological view with bubble chart
- **Top Movies:** Highest-rated films visualization

### Reports
- **Excel Report:** Multi-sheet analysis with formatting
- **Markdown Report:** Detailed findings and insights
- **JSON Data:** Raw and processed datasets

## 🎯 Methodology

1. **Data Collection:** Sourced from IMDb advanced search
2. **Filtering:** Applied strict quality and popularity criteria
3. **Validation:** Verified all entries meet requirements
4. **Analysis:** Statistical analysis and trend identification
5. **Visualization:** Created charts and graphs for insights
6. **Reporting:** Generated comprehensive documentation

## 📋 Dataset Details

The dataset includes:
- **Movie Title** and **Release Year**
- **IMDb Rating** (7.8-9.0 range)
- **Vote Count** (10K+ votes)
- **Duration** information
- **Ranking** based on rating

## 🔍 Key Insights

### Quality Trends
- Consistent high quality across all entries (8.0+ average)
- Recent years show continued excellence
- Strong representation across multiple decades

### Popular Appeal
- Wide range of vote counts (11K to 898K)
- Balance between critical acclaim and mass appeal
- International recognition evident in vote numbers

### Temporal Distribution
- **2000s:** 34 movies (34%)
- **2010s:** 47 movies (47%)
- **2020s:** 19 movies (19%)

## 🛠️ Technical Details

- **Language:** Python 3.x
- **Libraries:** pandas, matplotlib, seaborn, openpyxl
- **Data Format:** JSON, Excel, PNG
- **Analysis Type:** Descriptive statistics, data visualization

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

## 📞 Contact

For questions or suggestions about this analysis, please open an issue in this repository.

---

*This analysis celebrates the excellence of Indian cinema and provides insights into the highest-quality films of the 21st century.*

