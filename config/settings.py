import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
LOGS_DIR = PROJECT_ROOT / "logs"

# Create directories
RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)
LOGS_DIR.mkdir(parents=True, exist_ok=True)

# Region settings (South East England)
REGION_NAME = "South East England"
REGION_LAT = 51.0
REGION_LON = -0.5

# API Keys (from .env file)
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY", "")
AIQ_API_KEY = os.getenv("AIQ_API_KEY", "")

# Settings
DEBUG_MODE = True
LOG_LEVEL = "INFO"
TEMPERATURE_UNIT = "Celsius"