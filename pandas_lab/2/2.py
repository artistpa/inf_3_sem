import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("flights.csv", delimiter=',', index_col=0)
print(df)
print(df["CARGO"].value_counts())
print(df.groupby(by = "CARGO").sum())
'''print("Full price for Nimble =", df[df["CARGO"] == "Nimble"]["PRICE"].sum())
print("Full price for Medium =", df[df["CARGO"] == "Medium"]["PRICE"].sum())
print("Full price for Jumbo =", df[df["CARGO"] == "Jumbo"]["PRICE"].sum())
print("Full weight for Nimble =", df[df["CARGO"] == "Nimble"]["WEIGHT"].sum())
print("Full weight for Medium =", df[df["CARGO"] == "Medium"]["WEIGHT"].sum())
print("Full weight for Jumbo =", df[df["CARGO"] == "Jumbo"]["WEIGHT"].sum())'''

'''fig, axs = plt.subplots(1,3)
companies = ["Nimble", "Medium", "Jumbo"]
numbers = [500, 100, 50]
prices = [752588, 36312, 76795]
weights = [7545, 9507, 18709]
axs[0].pie(numbers, labels=companies, textprops={'size': 'smaller'}, radius=1)
axs[1].pie(prices, labels=companies, textprops={'size': 'smaller'}, radius=1)
axs[2].pie(weights, labels=companies, textprops={'size': 'smaller'}, radius=1)
axs[0].set_title("Numbers", fontsize = 10, pad = 14)
axs[1].set_title("Prices", fontsize = 10, pad = 14)
axs[2].set_title("Weights", fontsize = 10, pad = 14)'''
(df["CARGO"].value_counts()).plot.pie(figsize=(5,5))
plt.savefig("Numbers.jpg")
(df.groupby(by = "CARGO").sum()).plot.pie(y="PRICE", figsize=(5,5))
plt.savefig("Prices.jpg")
(df.groupby(by = "CARGO").sum()).plot.pie(y="WEIGHT", figsize=(5,5))
plt.savefig("Weight.jpg")