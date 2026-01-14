import pandas as pd
from pathlib import Path


#Paths
RAW_DATA_PATH = Path("data\\raw\\ecommerce_sales_data.csv")
CLEAN_DATA_PATH = Path("data\\processed\\cleaned _data.csv")

df = pd.read_csv(RAW_DATA_PATH)

#print(df.head())
#print(df.info())

print("Before: ",len(df))

#Remove duplicates
df.drop_duplicates(inplace=True)

#Check duplicates
print("After: ",len(df))
print(df.duplicated().sum())
print(df.duplicated(subset=["order_id", "product", "order_date"]).sum())

#Fix Date column
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df.dropna(subset=["order_date"], inplace=True) #Completely remove missing dates

#Check for missing values
print(df[["product", "quantity", "price", "region"]].isna().sum())

critical_cols = ["product", "quantity", "price", "region"]

df.dropna(subset = critical_cols, inplace=True)

df["category"] = df["category"].fillna("Unknown")

#Standardize data
for col in ["product","region","category"]:
    df[col] = df[col].str.strip().str.title()

#Fix Data Types
df["price"] = pd.to_numeric(df["price"], errors="coerce")
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
df.dropna(subset=["price","quantity"], inplace=True) #Removes rows with missing values

#Feature Engineering
df["revenue"] = df["quantity"] * df["price"]
df["month"] = df["order_date"].dt.to_period("M").astype(str)

#Save clean data
CLEAN_DATA_PATH.parent.mkdir(parents = True, exist_ok = True)
df.to_csv(CLEAN_DATA_PATH, index=False)

print("Cleaned Data Saved Sucessfully!")
print(f"Final rows {len(df)}")
