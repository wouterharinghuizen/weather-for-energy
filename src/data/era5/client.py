import cdsapi
import os
from pathlib import Path
from dotenv import load_dotenv


CDS_API_URL = "https://cds.climate.copernicus.eu/api"
REPO_ROOT = Path(__file__).resolve().parents[3]

load_dotenv(REPO_ROOT / ".env")
ERA5_CDS_API_KEY = os.getenv("ERA5_CDS_API_KEY")

client = cdsapi.Client(url=CDS_API_URL, key=ERA5_CDS_API_KEY)

dataset = "reanalysis-era5-pressure-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": ["geopotential"],
    "year": ["2024"],
    "month": ["03"],
    "day": ["01"],
    "time": ["13:00"],
    "pressure_level": ["550"],
    "data_format": "grib",
}
target = REPO_ROOT / "data/era5/example.grib"

client.retrieve(dataset, request, target)
