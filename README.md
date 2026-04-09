🛍️ Customer Shopping Behavior Analysis
An end-to-end data analytics project analyzing customer shopping behavior across 3,900 transactions using Python, SQL, and Power BI.

📌 Project Overview
This project uncovers insights into customer spending patterns, product preferences, discount behavior, and subscription trends to support data-driven business decisions.

🗂️ Repository Structure
customer-shopping-behavior/
│
├── customer_shopping_behavior.csv       # Raw dataset
├── Customer_Behavior_Analysis.py        # Python EDA & cleaning script
├── Customer_Shopping_Analysis.sql       # SQL business queries
├── Customer_Shopping_Behavior_Analysis_Report.docx  # Full project report
├── CBD.png                              # Power BI dashboard screenshot
└── README.md

🔧 Tools & Technologies
ToolPurposePython (pandas, numpy)Data cleaning & feature engineeringSQLAlchemy + PyMySQLPython → MySQL connectionMySQL / PostgreSQLBusiness intelligence queriesPower BIInteractive dashboardJupyter NotebookEDA development environment

🧹 Data Preprocessing (Python)

Loaded dataset with 3,900 rows and 18 columns
Imputed 37 missing Review Rating values using category-wise median
Standardized column names to snake_case
Engineered new features:

age_group — quartile-based age bins (Young Adult / Adult / Middle Aged / Senior)
purchase_frequency_days — numeric conversion of purchase frequency strings


Dropped redundant promo_code_used column (identical to discount_applied)
Exported cleaned data to MySQL via SQLAlchemy


📊 SQL Analysis — Business Questions
#QuestionQ1Revenue by GenderQ2High-spending discount users (above average spend)Q3Top 5 products by average review ratingQ4Average purchase amount: Standard vs Express shippingQ5Subscribers vs Non-Subscribers — spend & revenueQ6Top 5 discount-dependent productsQ7Customer segmentation: New / Returning / LoyalQ8Top 3 products per categoryQ9Repeat buyers (>5 purchases) and subscription likelihoodQ10Revenue contribution by age group

📈 Key Findings

👨 Male customers generate 2.1x more revenue than female customers ($157,890 vs $75,191)
🏅 80% of customers are Loyal (>10 previous purchases)
💳 Only 27% of customers subscribe, yet subscription conversion among repeat buyers remains low — a major growth opportunity
🎩 Hats and Sneakers have ~50% discount rates, suggesting potential margin risk
🧤 Gloves, Sandals, and Boots are the highest-rated products
🧑‍🤝‍🧑 Young Adults contribute the most revenue ($62,143)


📉 Power BI Dashboard
Show Image
Features dynamic filters for Subscription Status, Gender, Category, and Shipping Type.

💡 Business Recommendations

Boost subscriptions — target repeat buyers with exclusive perks
Formalize loyalty programs — convert Returning customers to Loyal
Review discount strategy — reduce dependency for Hat, Sneakers, Coat
Upsell Express shipping users — they spend more on average
Promote top-rated products — Gloves, Sandals, Boots in campaigns
Target Young Adults — highest revenue segment
Close the gender gap — develop female-targeted marketing initiatives


🚀 How to Run
Python (EDA & Cleaning):
bashpip install pandas numpy sqlalchemy pymysql
jupyter notebook Customer_Behavior_Analysis.py
SQL:
sqlCREATE DATABASE customer_shopping;
USE customer_shopping;
-- Run Customer_Shopping_Analysis.sql

⚠️ Update the database credentials in the Python script before running:
pythonengine = create_engine("mysql+pymysql://your_user:your_password@localhost/customer_shopping")


👩‍💻 Author
Tanvi Thopte

This project was built for learning and portfolio purposes.