# Gender Pay Equality Analysis

## 📊 Project Overview
Analyzed salary equality across 37 job roles in Daikibo's 4 factories to identify gender pay gaps and classify roles by equality severity.

## 🎯 Objectives
Create a classification system to identify and prioritize gender pay inequality across:
- 4 global factory locations
- 11 job role levels (C-Level to Machine Operator)
- 37 unique role-factory combinations

## 📈 Key Findings
- **51.4% Fair** - Within acceptable equality range (±10 points)
- **29.7% Unfair** - Moderate inequality requiring attention
- **18.9% Highly Discriminative** - Severe inequality requiring immediate action

### Problem Areas:
- **Worst Factory:** Daikibo Factory Meiyo (avg score: -14.5)
- **Worst Job Roles:** C-Level (-25), VP (-26), Senior Management (-15 to -21)
- **Critical Finding:** Gender pay inequality increases at higher organizational levels

## 🛠️ Technologies Used
- **Python 3.x**
- **Pandas** - Data analysis
- **Matplotlib** - Multi-panel dashboard visualization
- **NumPy** - Statistical calculations
- **Excel** - Data processing

## 📊 Classification Logic
Equality scores classified into three categories:
- **Fair:** -10 to +10 (acceptable range)
- **Unfair:** -20 to -11 OR +11 to +20 (moderate concern)
- **Highly Discriminative:** Below -20 OR above +20 (severe inequality)

## 🔍 Methodology
1. Load and validate equality scores
2. Apply classification algorithm
3. Aggregate by factory and job role
4. Statistical analysis and distribution
5. Multi-dimensional visualization
6. Generate actionable recommendations

## 📁 Files
- `equality_analysis.py` - Complete Python analysis code
- `screenshots/` - 6-panel dashboard visualization

## 📊 Results
Comprehensive 6-panel dashboard revealing inequality patterns across organizational hierarchy and factory locations.

## 💡 Recommendations
1. **Immediate:** Review VP and C-Level compensation at Meiyo and Seiko
2. **Short-term:** Implement pay transparency policies
3. **Medium-term:** Focus on senior management equality
4. **Long-term:** Quarterly audits with improvement targets
5. **Goal:** Move all "Highly Discriminative" cases to "Unfair" or better within 12 months

## 💼 Business Impact
Provides data-driven roadmap for achieving pay equity and regulatory compliance across global operations.
