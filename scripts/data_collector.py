import json
from datetime import datetime
from pathlib import Path
import pandas as pd
from config.settings import RAW_DATA_DIR, REGION_NAME, REGION_LAT, REGION_LON, WEATHER_API_KEY

class EnvironmentalDataCollector:
    """Collects environmental data for South East England"""
    
    def __init__(self):
        self.region_name = REGION_NAME
        self.latitude = REGION_LAT
        self.longitude = REGION_LON
        self.weather_data = []
        print(f" Initialized collector for {self.region_name}")
    
    def collect_weather_data(self):
        """Collect weather data"""
        try:
            print(f"📊 Collecting weather data for {self.region_name}...")
            
            # Example data structure (replace with real API call)
            weather = {
                "timestamp": datetime.now().isoformat(),
                "region": self.region_name,
                "temperature": 15.5,
                "humidity": 65,
                "pressure": 1013,
                "wind_speed": 8.5,
                "description": "Partly cloudy"
            }
            
            self.weather_data.append(weather)
            print("✓ Weather data collected")
            return weather
            
        except Exception as e:
            print(f"✗ Error collecting weather: {e}")
            return None
    
    def save_to_csv(self, filename):
        """Save data to CSV"""
        try:
            if not self.weather_data:
                print("✗ No data to save")
                return False
            
            df = pd.DataFrame(self.weather_data)
            output_path = RAW_DATA_DIR / filename
            df.to_csv(output_path, index=False)
            print(f"✓ Data saved to {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error saving data: {e}")
            return False
    
    def save_to_json(self, filename):
        """Save data to JSON"""
        try:
            output_path = RAW_DATA_DIR / filename
            with open(output_path, 'w') as f:
                json.dump(self.weather_data, f, indent=2)
            print(f"✓ Data saved to {output_path}")
            return True
            
        except Exception as e:
            print(f"✗ Error saving JSON: {e}")
            return False


def main():
    collector = EnvironmentalDataCollector()
    collector.collect_weather_data()
    collector.save_to_csv("weather_data.csv")
    collector.save_to_json("weather_data.json")


if __name__ == "__main__":
    main()