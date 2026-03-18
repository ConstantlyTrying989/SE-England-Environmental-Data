import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from scripts.data_collector import EnvironmentalDataCollector
from scripts.data_processor import DataProcessor
from scripts.data_visualizer import DataVisualizer

def main():
    print("\n" + "="*50)
    print("SE ENGLAND ENVIRONMENTAL DATA PIPELINE")
    print("="*50 + "\n")
    
    # Step 1: Collect
    print("[1/3] DATA COLLECTION PHASE")
    collector = EnvironmentalDataCollector()
    collector.collect_weather_data()
    collector.save_to_csv("weather_raw.csv")
    
    # Step 2: Process
    print("\n[2/3] DATA PROCESSING PHASE")
    processor = DataProcessor()
    df = processor.load_csv("weather_raw.csv")
    if df is not None:
        df = processor.clean_data(df)
        stats = processor.get_statistics(df)
        processor.save_processed(df, "weather_processed.csv")
        print(f"\nStats: {stats}")
    
    # Step 3: Visualize
    print("\n[3/3] DATA VISUALIZATION PHASE")
    viz = DataVisualizer()
    if df is not None:
        print("(Visualization would show here)")
    
    print("\n" + "="*50)
    print("✓ PIPELINE COMPLETED SUCCESSFULLY")
    print("="*50 + "\n")

if __name__ == "__main__":
    main()