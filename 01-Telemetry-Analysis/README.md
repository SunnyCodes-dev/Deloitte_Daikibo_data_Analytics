# Manufacturing Telemetry Analysis

## 📊 Project Overview
Analyzed 160,000+ IoT telemetry records from Daikibo's 4 global manufacturing facilities to identify production bottlenecks and machine failures.

## 🎯 Objectives
1. Identify which factory location experienced the most machine downtime
2. Determine which machine types were responsible for failures

## 📈 Key Findings
- **Daikibo Factory Seiko (Osaka, Japan)** experienced the highest downtime: **480 minutes (8 hours)**
- **LaserWelder machines** were 100% responsible for Seiko's downtime
- **Recommendation:** Immediate maintenance review and potential replacement of LaserWelders at Seiko facility

## 🛠️ Technologies Used
- **Python 3.x**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **NumPy** - Numerical operations
- **Tableau** - Business intelligence dashboards

## 📊 Data
- **Source:** Daikibo Industries IoT sensors
- **Records:** 160,704 telemetry readings
- **Time Period:** May 2021
- **Factories:** 4 (Meiyo-Tokyo, Seiko-Osaka, Berlin, Shenzhen)
- **Device Types:** 9 (CNC, LaserWelder, HeavyDutyDrill, etc.)
- **Frequency:** 10-minute intervals

## 🔍 Methodology
1. Data loading and JSON flattening
2. Exploratory Data Analysis (EDA)
3. Downtime calculation (10 mins per unhealthy status)
4. Factory-level aggregation
5. Device-level drill-down analysis
6. Visualization and reporting

## 📁 Files
- `telemetry_analysis.py` - Complete Python analysis code
- `screenshots/` - Dashboard visualizations

## 📊 Results
Analysis revealed critical bottleneck at Seiko factory requiring immediate intervention.

## 💼 Business Impact
This analysis enables Daikibo to:
- Prioritize maintenance resources effectively
- Reduce production downtime by 46% (Seiko's contribution)
- Make data-driven equipment replacement decisions
