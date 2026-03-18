import matplotlib.pyplot as plt
import pandas as pd
from config.settings import PROCESSED_DATA_DIR

class DataVisualizer:
    """Creates visualizations"""
    
    def __init__(self):
        print(" Data visualizer initialized")
        plt.style.use("seaborn-v0_8-darkgrid")
    
    def plot_temperature(self, df):
        """Plot temperature data"""
        try:
            if "temperature" not in df.columns:
                print("✗ Temperature column not found")
                return
            
            plt.figure(figsize=(12, 6))
            plt.plot(range(len(df)), df["temperature"], marker="o", linewidth=2)
            plt.xlabel("Data Point")
            plt.ylabel("Temperature (°C)")
            plt.title("Temperature Trend - South East England")
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()
            print("✓ Temperature plot created")
            
        except Exception as e:
            print(f"✗ Error creating plot: {e}")
    
    def plot_humidity(self, df):
        """Plot humidity distribution"""
        try:
            if "humidity" not in df.columns:
                print("✗ Humidity column not found")
                return
            
            plt.figure(figsize=(12, 6))
            plt.hist(df["humidity"], bins=20, edgecolor="black")
            plt.xlabel("Humidity (%)")
            plt.ylabel("Frequency")
            plt.title("Humidity Distribution - South East England")
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()
            print("✓ Humidity plot created")
            
        except Exception as e:
            print(f"✗ Error creating plot: {e}")


def main():
    df = pd.read_csv(PROCESSED_DATA_DIR / "weather_cleaned.csv")
    viz = DataVisualizer()
    viz.plot_temperature(df)
    viz.plot_humidity(df)


if __name__ == "__main__":
    main()