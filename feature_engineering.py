import pandas as pd
import pandas_ta as ta

def add_features(df):
    df['RSI'] = ta.rsi(df['Close'], length=14)
    df['SMA20'] = ta.sma(df['Close'], length=20)
    df['Return'] = df['Close'].pct_change()
    df['Volatility'] = df['Return'].rolling(5).std()
    df['Target'] = (df['Close'].shift(-1) > df['Close']).astype(int)
    df.dropna(inplace=True)
    return df
