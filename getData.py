import pandas as pd
import requests
from influxdb import InfluxDBClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key
api_key = os.getenv('INFLUXDB_API_KEY')

if not api_key:
    raise ValueError("API key not found. Please ensure it is set in the .env file.")

def fetch_realtime_data(api_endpoint):
    headers = {'Authorization': f'Bearer {api_key}'}  # Add the API key to the request headers
    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()  # Check if the request was successful
    data = response.json()  # Assuming data comes in JSON format
    df = pd.DataFrame(data)
    print("Realtime data columns:", df.columns)  # Debugging line
    return df

def fetch_historical_data(csv_file_path):
    df = pd.read_csv(csv_file_path)
    print("Columns in historical_data.csv:", df.columns)  # Debugging line
    return df

def normalize_timestamps(df, timezone='EST'):
    print("DataFrame before normalization:", df.head())  # Debugging line
    if 'timestamp' in df.columns:
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df['timestamp'] = df['timestamp'].dt.tz_localize('UTC').dt.tz_convert(timezone)
        print("DataFrame after normalization:", df.head())  # Debugging line
    else:
        print("Timestamp column is missing in the DataFrame.")
    return df

def store_in_influxdb(df, measurement_name):
    client = InfluxDBClient(host='localhost', port=8086)
    client.switch_database('sma_data')
    
    json_body = []
    for index, row in df.iterrows():
        json_body.append({
            "measurement": measurement_name,
            "time": row['timestamp'].isoformat(),  # Ensure the timestamp is in the correct format
            "fields": {
                "open": row.get('open', 0),  # Use get() to provide a default value if the column is missing
                "high": row.get('high', 0),
                "low": row.get('low', 0),
                "close": row.get('close', 0),
                "volume": row.get('volume', 0)
            }
        })
    client.write_points(json_body)

# Example usage
realtime_data = fetch_realtime_data("https://api.lightspeed.com/v1/markets/realtime")
historical_data = fetch_historical_data("historical_data.csv")

realtime_data = normalize_timestamps(realtime_data)
historical_data = normalize_timestamps(historical_data)

store_in_influxdb(realtime_data, 'realtime_prices')
store_in_influxdb(historical_data, 'historical_prices')
