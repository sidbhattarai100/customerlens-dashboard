# CustomerLens — Customer Segmentation Dashboard

An AI-powered customer segmentation platform that identifies behavioral clusters from 2,240 customers using K-Means clustering, backed by AWS RDS and deployed on Streamlit Cloud.

🔗 **Live Demo:** [customerlens-sid.streamlit.app](https://customerlens-sid.streamlit.app)

---

## Overview

CustomerLens analyzes customer purchasing behavior across product categories (wine, meat, fruits, fish, sweets) and demographic data to segment customers into 4 distinct behavioral groups — enabling smarter, data-driven marketing decisions.

---

## Customer Segments Discovered

| Segment | Customers | Avg Income | Key Trait |
|---|---|---|---|
| 💎 Premium Shoppers | 346 | $77,591 | Highest wine & meat spend |
| 💰 Budget Shoppers | 1,035 | $35,007 | Low spend across all categories |
| 🌐 Online Middle Class | 546 | $57,143 | Highest web purchases |
| 🍽️ Gourmet Enthusiasts | 313 | $72,699 | Top fruit, fish & sweets spend |

---

## Tech Stack

| Layer | Tools |
|---|---|
| Data Processing | Python, Pandas, NumPy |
| Machine Learning | Scikit-learn, K-Means, PCA |
| Database | AWS RDS (MySQL) |
| Dashboard | Streamlit, Matplotlib, Seaborn |
| Deployment | Streamlit Cloud |
| Version Control | Git, GitHub |

---

## Methodology

1. **Data Collection** — Customer Personality Analysis dataset (2,240 rows, 29 features)
2. **Data Cleaning** — Imputed 24 missing income values, removed duplicates
3. **Feature Engineering** — Selected 11 behavioral and demographic features
4. **Scaling** — StandardScaler applied before clustering
5. **Clustering** — K-Means with elbow method (k=4) and PCA for visualization
6. **Storage** — Clean data and cluster labels pushed to AWS RDS
7. **Dashboard** — Interactive Streamlit app deployed publicly

---

## Key Insights

- **Budget Shoppers** make up 46% of customers but have the lowest spend — ideal for discount campaigns
- **Premium Shoppers** have the highest income ($77K) and dominate wine & meat — ideal for loyalty programs
- **Online Middle Class** leads in web purchases — best segment for digital marketing
- **Gourmet Enthusiasts** are a niche high-value group — perfect for specialty product upsells

---

## Run Locally
```bash
git clone https://github.com/sidbhattarai100/customerlens-dashboard.git
cd customerlens-dashboard
pip install -r requirements.txt
streamlit run app.py
```

---

## Dataset

[Customer Personality Analysis](https://www.kaggle.com/datasets/imakash3011/customer-personality-analysis) — Kaggle

---

## Author

**Siddhartha Bhattarai**
- Portfolio: [sidbhattarai100.github.io](https://sidbhattarai100.github.io)
- GitHub: [@sidbhattarai100](https://github.com/sidbhattarai100)
