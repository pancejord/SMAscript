import matplotlib.pyplot as plt

def plot_sma_signals(df):
    plt.figure(figsize=(14, 7))
    plt.plot(df['timestamp'], df['close'], label='Close Price')
    for window in windows:
        plt.plot(df['timestamp'], df[f'SMA_{window}'], label=f'SMA_{window}')
    
    buy_signals = df[df['Signal'] == 1]
    sell_signals = df[df['Signal'] == -1]
    
    plt.scatter(buy_signals['timestamp'], buy_signals['close'], label='Buy Signal', marker='^', color='green')
    plt.scatter(sell_signals['timestamp'], sell_signals['close'], label='Sell Signal', marker='v', color='red')
    
    plt.title('SMA and Trading Signals')
    plt.legend()
    plt.show()

# Example usage
plot_sma_signals(sma_df)
