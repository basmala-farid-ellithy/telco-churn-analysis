"""Telco customer churn analysis: who leaves, and what do they have in common."""
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

URL = "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/master/data/Telco-Customer-Churn.csv"
df = pd.read_csv(URL)  # public IBM sample dataset
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df = df.dropna(subset=["TotalCharges"])  # 11 new customers with blank totals
df["churn"] = (df["Churn"] == "Yes").astype(int)
df["tenure_band"] = pd.cut(df["tenure"], [-1, 12, 24, 48, 72],
                           labels=["0-12m", "13-24m", "25-48m", "49-72m"])

lines = [f"Customers: {len(df)}", f"Overall churn rate: {df.churn.mean():.1%}",
         f"Monthly revenue lost to churners: ${df.loc[df.churn == 1, 'MonthlyCharges'].sum():,.0f} "
         f"of ${df.MonthlyCharges.sum():,.0f}", ""]
for col in ["Contract", "InternetService", "PaymentMethod", "tenure_band", "SeniorCitizen"]:
    t = df.groupby(col, observed=True).churn.agg(["count", "mean"])
    t["mean"] = (t["mean"] * 100).round(1)
    lines += [f"Churn % by {col}", t.rename(columns={"count": "customers", "mean": "churn_pct"}).to_string(), ""]
open("results.txt", "w").write("\n".join(lines))
print("\n".join(lines))

fig, ax = plt.subplots(1, 3, figsize=(14, 4))
for a, col in zip(ax, ["Contract", "tenure_band", "PaymentMethod"]):
    (df.groupby(col, observed=True).churn.mean() * 100).plot.bar(ax=a, color="#2b6cb0")
    a.set_title(f"Churn % by {col}"); a.set_ylabel("%"); a.tick_params(axis="x", rotation=25)
plt.tight_layout(); plt.savefig("churn_drivers.svg", format="svg")
