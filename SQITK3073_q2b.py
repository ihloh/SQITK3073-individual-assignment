import pandas as pd

df = pd.read_csv("stock_data.csv")

# classify each stock
def classify(x):
    if x < 0:
        return "Negative Return"
    elif x <= 2:
        return "Moderate Return"
    else:
        return "High Return"

df["Performance Category"] = df["Return Percentage (%)"].apply(classify)
print(df[["Ticker",
          "Previous Closing Price (RM)",
          "Latest Closing Price (RM)",
          "Estimated Total Return (RM)",
          "Return Percentage (%)",
          "Performance Category"
        ]].to_string(index=False))

group_result = df.groupby("Performance Category")["Estimated Total Return (RM)"].mean()
group_result = "RM " + group_result.round(2).astype(str)
print("\n" ,group_result.to_string())