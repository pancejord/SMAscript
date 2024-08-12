from functools import lru_cache
from concurrent.futures import ThreadPoolExecutor

@lru_cache(maxsize=1000)
def fetch_cached_data(api_endpoint):
    return fetch_realtime_data(api_endpoint)

def parallel_sma_calculation(df, windows):
    with ThreadPoolExecutor() as executor:
        results = executor.map(calculate_sma, [df] * len(windows), windows)
    return results

# Example usage
realtime_data = fetch_cached_data("https://api.lightspeed.com/v1/markets/realtime")
parallel_sma_results = parallel_sma_calculation(realtime_data, windows)
