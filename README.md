# Social Media Analytics Data Warehouse

## 📌 Project Overview
This project simulates a **Data Warehouse (DWH)** for a social media analytics platform (Instagram, YouTube, Meta).  
The goal is to design a **scalable data model**, build **ETL pipelines**, and create **dashboards** for user growth, engagement, and revenue.

---

## ⚙️ Tech Stack
- **PostgreSQL** (Docker) → Data Warehouse
- **Python (pandas, sqlalchemy)** → ETL scripts
- **Airflow** → Workflow orchestration (future step)
- **dbt** → Data modeling & transformations (future step)
- **Metabase / Power BI** → Analytics dashboards (future step)

---

## 📂 Project Structure
social-media-analytics-dwh/
│
├── README.md # Project description and instructions
├── docker-compose.yml # Docker setup for PostgreSQL
│
├── sql/ # SQL scripts
│ ├── create_tables.sql # DWH table creation script
│ └── sample_inserts.sql # Sample data inserts
│
├── data/ # Raw/mock datasets
│ ├── users.csv
│ ├── posts.csv
│ ├── engagements.csv
│ └── ads.csv
│
├── etl/ # Python ETL scripts
│ ├── load_users.py
│ ├── load_posts.py
│ ├── load_engagements.py
│ └── load_ads.py
│
├── airflow/ # Airflow DAGs (for automation, later)
│ └── dags/
│
└── dashboards/ # BI dashboards / screenshots
├── user_growth.png
├── engagement_dashboard.png
└── revenue_dashboard.png


## 🗄️ Data Model (Star Schema)
**Dimensions (descriptive info):**
- `dim_users` → user info (user_id, country, signup_date, device)
- `dim_posts` → post info (post_id, user_id, platform, post_type)
- `dim_ads` → ad campaign info

**Facts (measurable events):**
- `fact_engagements` → likes, comments, shares, views (linked to posts/users)
- `fact_ads_performance` → impressions, clicks, conversions, spend, revenue

---




https://chatgpt.com/share/68b56b9e-5394-8011-b157-b4444a588073
