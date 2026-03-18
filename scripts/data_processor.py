import pandas as pd
from config.settings import RAW_DATA_DIR, PROCESSED_DATA_DIR

class DataProcessor:
    """Processes environmental data"""
    
    def __init__(self):
        print(" Data processor initialized")
    
    def load_csv(self, filename):
        """Load CSV file"""
        try:
            filepath = RAW_DATA_DIR / filename
            df = pd.read_csv(filepath)
            print(f"✓ Loaded {filename}")
            return df
        except Exception as e:
            print(f"✗ Error loading {filename}: {e}")
            return None
    
    def clean_data(self, df):
        """Clean and process data"""
        # Remove duplicates
        df = df.drop_duplicates()
        # Remove rows with missing values
        df = df.dropna()
        print("✓ Data cleaned")
        return df
    
    def get_statistics(self, df):
        """Calculate basic statistics"""
        stats = {
            "mean_temp": df["temperature"].mean() if "temperature" in df else 0,
            "max_temp": df["temperature"].max() if "temperature" in df else 0,
            "min_temp": df["temperature"].min() if "temperature" in df else 0,
        }
        return stats
    
    def save_processed(self, df, filename):
        """Save processed data"""
        try:
            filepath = PROCESSED_DATA_DIR / filename
            df.to_csv(filepath, index=False)
            print(f"✓ Saved to {filename}")
            return True
        except Exception as e:
            print(f"✗ Error saving: {e}")
            return False


def main():
    processor = DataProcessor()
    df = processor.load_csv("weather_data.csv")
    if df is not None:
        df = processor.clean_data(df)
        stats = processor.get_statistics(df)
        processor.save_processed(df, "weather_cleaned.csv")
        print("\nStatistics:")
        for key, value in stats.items():
            print(f"  {key}: {value:.2f}")


if __name__ == "__main__":
    main()