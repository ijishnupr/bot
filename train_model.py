import yfinance as yf

symbol = "COCHINSHIP.NS"
data = yf.download(tickers=symbol, interval="5m", period="5d")
data.dropna(inplace=True)
data.to_csv("cochinship_5min.csv")
