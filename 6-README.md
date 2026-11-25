# Telco Customer Churn Analysis

Python (pandas + matplotlib) analysis of the public IBM Telco customer churn dataset (7,043 customers, 21 columns). Question: which customers leave, and where should a retention team focus?

## Key findings
- Overall churn is **26.6%**. Churners account for about **$139K of $456K** monthly revenue (30.5%).
- **Contract type** is the strongest signal: month-to-month 42.7%, one-year 11.3%, two-year 2.8%.
- **New customers** churn most: 47.7% in the first 12 months vs 9.5% after 4 years.
- **Fiber optic** customers churn at 41.9% (DSL 19.0%). **Electronic check** payers churn at 45.3% vs about 16% for automatic payment.
- Senior citizens churn at 41.7% vs 23.7%.

## Recommendations
1. Offer incentives to move month-to-month customers to annual contracts in their first year.
2. Push automatic payment at signup.
3. Review fiber optic service quality and pricing.

![drivers](charts/churn_drivers.png)

## Run it
```
pip install pandas matplotlib
python analysis.py
```
Outputs `results.txt` and `charts/churn_drivers.png`. 11 rows with blank TotalCharges (brand-new customers) are dropped.

Data: https://github.com/IBM/telco-customer-churn-on-icp4d (public sample data).
