import pandas as pd
import matplotlib as plt
from matplotlib import pyplot as plt

df = pd.read_csv("stock_data.csv")

plt.figure(figsize=(10,6))

plt.bar(df["Ticker"], df["Return Percentage (%)"])

plt.title("Portfolio Return Percentage Comparison")
plt.xlabel("Stocks")
plt.ylabel("Return Percentage (%)")

plt.show()