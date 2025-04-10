import matplotlib.pyplot as plt

def backtest(df, model, features):
    df['Pred'] = model.predict(df[features])
    df['Signal'] = df['Pred'].shift(1)
    df['Strategy_Return'] = df['Signal'] * df['Return']
    cumulative = (1 + df['Strategy_Return']).cumprod()

    plt.figure(figsize=(12, 6))
    plt.plot((1 + df['Return']).cumprod(), label='Market Return')
    plt.plot(cumulative, label='Strategy Return')
    plt.legend()
    plt.title('Backtest')
    plt.show()
