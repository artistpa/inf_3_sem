import pandas as pd

df = pd.read_csv("transactions.csv", delimiter=',', index_col=0)
df = df.sort_values(by="SUM", ascending=False)
print(df)
print(df[df["STATUS"] == "OK"]. head(3))
dfu = df[(df["CONTRACTOR"] == "Umbrella, Inc") & (df["STATUS"] == "OK")]
print("SUM for Umbrella, Inc = ", dfu["SUM"].sum())
