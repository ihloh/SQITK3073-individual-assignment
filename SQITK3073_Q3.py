import yfinance as yf
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

stocks = {
    "Maybank": "1155.KL",
    "Tenaga": "5347.KL",
    "PBBANK": "1295.KL",
    "CIMB": "1023.KL",
    "IHH": "5225.KL"
}

plt.figure(figsize=(12,6))

start_date = "2026-03-01"
end_date = "2026-04-01"

for company, ticker in stocks.items():
    data = yf.download(ticker, start=start_date, end=end_date, progress=False)
    plt.plot(data.index, data["Close"], label=company)

plt.title("Bursa Malaysia Stocks - MARCH 2026 Closing Price Trend")
plt.xlabel("Date")
plt.ylabel("Closing Price (RM)")
plt.legend()
plt.grid()

plt.show()