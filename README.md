# 📊 Marketing Campaign Analysis Project

## 🔎 Overview
This project analyzes customer data from a marketing campaign to uncover insights, segment customers, and build an interactive dashboard for decision‑making.  
It combines **Python (Pandas, Seaborn, Plotly)**, **MySQL Workbench**, and **Streamlit** to deliver a complete end‑to‑end solution.

---

## 🛠️ Project Workflow
1. **Data Preparation & Cleaning**  
   - Handle missing values  
   - Feature engineering (Age, Children, Total Spend, Tenure, etc.)  
   - Save cleaned dataset  

2. **Exploratory Data Analysis (EDA)**  
   - Distributions (Age, Income, Spend)  
   - Response vs demographics  
   - Correlation heatmaps  
   - Channel usage patterns  

3. **Segmentation**  
   - Rule‑based flags: High Income, Young Customer, Campaign Responder, High Web Engagement, Family Customer, High Spender  
   - Save segmented dataset  

4. **SQL Integration**  
   - Load data into MySQL (`marketing_campaign` database)  
   - Create `customers` table schema  
   - Run analytical queries (response rate, avg spend, channel usage)  

5. **Interactive Dashboard (Streamlit)**  
   - Sidebar filters (Country, Education, Marital Status, Income)  
   - KPIs (Response Rate, Avg Spend, Avg Web Visits, Avg Age)  
   - Charts: Spending patterns, Channel usage, Campaign performance, Age vs Spend trend  
   - Download filtered data  

6. **Insights & Recommendations**  
   - High spenders respond better to campaigns  
   - Web channel is strong among valuable customers  
   - Family households show higher spending  
   - Target profile: Age 30–45, income > ₹75,000, family households  

7. **Deliverables**  
   - Jupyter notebooks (cleaning, EDA, segmentation)  
   - SQL scripts (schema + queries)  
   - Streamlit app (`app.py`)  
   - Project report with insights  
   - README.md (this file)  

---

## ⚙️ Setup Instructions

### Prerequisites
- Python 3.9+  
- MySQL Workbench  
- Streamlit  

### Install Dependencies
```bash
pip install pandas numpy matplotlib seaborn plotly mysql-connector-python streamlit
