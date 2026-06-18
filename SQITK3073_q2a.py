import pandas as pd

df = pd.read_csv("stock_data.csv")

# Question 2a - Portfolio Summary Table
portfolio_summary_table = df[[
    "Ticker",
    "Previous Closing Price (RM)",
    "Latest Closing Price (RM)",
    "Estimated Total Return (RM)",
    "Return Percentage (%)"
]]

print("\n===== PORTFOLIO SUMMARY =====\n")
print(portfolio_summary_table.to_string(index=False))