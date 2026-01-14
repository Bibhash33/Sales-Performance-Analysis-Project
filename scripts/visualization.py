import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

TABLES_PATH = Path("outputs/tables")
CHARTS_PATH = Path("outputs/charts")

monthly_sales = pd.read_csv(TABLES_PATH/"monthly_sales.csv")
revenue_by_region = pd.read_csv(TABLES_PATH/"revenue_by_region.csv")
top_products = pd.read_csv(TABLES_PATH/"top_products.csv")

#Monthly sales trend
plt.figure()
plt.plot(monthly_sales["month"],monthly_sales["revenue"])
plt.title("Monthly sales trend")
plt.xlabel("month")
plt.ylabel("revenue")
plt.xticks(rotation = 45)
plt.tight_layout()
plt.savefig(CHARTS_PATH/"monthly_sales.png")
plt.close()

#Best selling products
plt.figure()
plt.barh(top_products["product"],top_products["revenue"])
plt.title("Top 10 Products")
plt.xlabel("Revenue")
plt.ylabel("Product")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(CHARTS_PATH/"top_products.png")
plt.close()

#Revenue by region
plt.figure()
plt.bar(revenue_by_region["region"],revenue_by_region["revenue"])
plt.title("Revenue by region")
plt.xlabel("Region")
plt.ylabel("Revenue")
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig(CHARTS_PATH/"revenue_by_regions.png")
plt.close()

print("Visualizations saved sucessfully!")