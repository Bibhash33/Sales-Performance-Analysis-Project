import pandas as pd
from pathlib import Path

CLEAN_DATA_PATH = Path("data/processed/cleaned _data.csv")
OUTPUT_TABLE = Path("outputs/tables")

#Load Data
df = pd.read_csv(CLEAN_DATA_PATH)


#Monthly sales trend
monthly_sales = (df.groupby("month" ,as_index=False)["revenue"].sum().sort_values("month"))

#Best Selling Products
top_products = (df.groupby("product", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False).head(10))

#Revenue by Regions
revenue_by_region = (df.groupby("region", as_index=False)["revenue"].sum().sort_values("revenue", ascending=False))

#Save summary Tables
OUTPUT_TABLE.mkdir(parents=True, exist_ok=True)
monthly_sales.to_csv(OUTPUT_TABLE/"monthly_sales.csv", index = False)
top_products.to_csv(OUTPUT_TABLE/"top_products.csv", index = False)
revenue_by_region.to_csv(OUTPUT_TABLE/"revenue_by_region.csv", index = False)

print("Analysis Completed Sucessfully!")