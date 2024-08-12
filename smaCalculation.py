def calculate_sma(df, window):
    return df['close'].rolling(window=window).mean()

def compute_smas(df, windows):
    for window in windows:
        df[f'SMA_{window}'] = calculate_sma(df, window)
    return df

# Example usage
windows = [10, 50, 200]
sma_df = compute_smas(realtime_data, windows)
