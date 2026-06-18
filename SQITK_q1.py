import yfinance as yf
import pandas as pd

stocks = {
    "Maybank": "1155.KL",
    "Tenaga Nasional Berhad": "5347.KL",
    "Public Bank Berhad": "1295.KL",
    "CIMB Group Holdings Berhad": "1023.KL",
    "IHH Healthcare Berhad": "5225.KL"
}

results = []

start_date = "2026-03-01"
end_date = "2026-04-01"

for company, ticker in stocks.items():
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)

    close_prices = data["Close"].squeeze()

    # yesterday close
    yesterday_close = float(close_prices.iloc[-2])

    # today close
    today_close = float(close_prices.iloc[-1])

    # daily return
    daily_return = today_close - yesterday_close

    # shares purchasable
    shares = float(1000 // yesterday_close)

    # estimated total return
    estimated_return = daily_return * shares

    # return percentage
    return_percentage = (estimated_return / 1000) * 100

    results.append({
        "Ticker": company,
        "Previous Closing Price (RM)": round(yesterday_close, 2),
        "Latest Closing Price (RM)": round(today_close, 2),
        "Daily Return (RM)": round(daily_return, 2),
        "Shares Purchasable": shares,
        "Estimated Total Return (RM)": round(estimated_return, 2),
        "Return Percentage (%)": round(return_percentage, 2)
    })

df = pd.DataFrame(results)
print(df.to_string(index=False))
df.to_csv("stock_data.csv", index=False)