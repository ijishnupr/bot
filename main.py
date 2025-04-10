import fetch_data
from feature_engineering import add_features
import train_model 
from backtest import backtest

symbol = "COCHINSHIP.NS"
features = ['RSI', 'SMA20', 'Return', 'Volatility']

# Workflow
df = fetch_data(symbol)
df = add_features(df)
model = train_model(df, features)
backtest(df, model, features)
