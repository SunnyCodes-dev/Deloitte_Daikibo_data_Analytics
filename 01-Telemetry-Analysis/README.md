# Manufacturing Telemetry Analysis

This project analyzes over **160,000+ telemetry records** from Daikibo’s four manufacturing facilities.  
The goal is to understand machine performance, detect failures, and identify where production slowdowns occur.

---

## 🚀 Objectives
- Identify which factory had the **most machine downtime**
- Determine which **machine types** contributed most to the downtime

---

## 📊 Key Findings
- **Seiko Factory (Osaka, Japan)** recorded the **highest downtime (~480 minutes)**  
- Most of this downtime was caused by **LaserWelder machines**

### 🔧 Recommendation
Frequent maintenance checks are suggested for LaserWelder machines at the Seiko plant, especially monitoring temperature readings and performance patterns.

---

## 🛠 Technologies Used
- **Python**
- **Pandas** – data cleaning, handling duplicates/missing values, sorting, statistics
- **Matplotlib** – bar charts, horizontal bar charts, box plots
- **Tableau** – downtime analysis and breakdown visualization

---

## 📁 Data Summary
- **Total Records:** ~160,000  
- **Factories:** Tokyo (Meiyo), Osaka (Seiko), Berlin, Shenzhen  
- **Machine Types:** 9 (CNC, LaserWelder, HeavyDutyDrill, AirWrench, ConveyorBelt, Furnace, MetalPress, SpotWelder and LaserCutter)  
- **Frequency:** Every 10 minutes  
- **Format:** Nested JSON → Flattened into DataFrame  

---

## 🔍 Approach
1. Loaded and flattened nested JSON telemetry data  
2. Performed exploratory data analysis (EDA)  
3. Calculated downtime using *unhealthy* machine status (each = 10 minutes)  
4. Aggregated downtime by **factory** and by **machine type**  
5. Created visualizations to support insights  
6. Documented findings and prepared `telemetry_analysis.py`

---

## ✅ Conclusion
The analysis shows that the **Seiko factory** has the highest downtime, mainly due to **LaserWelder machines**.  
Focusing on maintenance and monitoring at this facility may significantly improve overall production efficiency.

---
