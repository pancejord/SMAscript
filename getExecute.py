def generate_signals(df):
    df['Signal'] = 0
    
    for i in range(1, len(df)):
        if df['SMA_10'].iloc[i] > df['SMA_50'].iloc[i] and df['SMA_10'].iloc[i-1] <= df['SMA_50'].iloc[i-1]:
            df['Signal'].iloc[i] = 1  # Buy signal
        elif df['SMA_10'].iloc[i] < df['SMA_50'].iloc[i] and df['SMA_10'].iloc[i-1] >= df['SMA_50'].iloc[i-1]:
            df['Signal'].iloc[i] = -1  # Sell signal
    return df

# Example usage
sma_df = generate_signals(sma_df)
