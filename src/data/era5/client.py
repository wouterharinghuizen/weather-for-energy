import cdsapi
import os
from pathlib import Path
from dotenv import load_dotenv

CDS_API_URL = "https://cds.climate.copernicus.eu/api"
REPO_ROOT = Path(__file__).resolve().parents[3]


class Era5DataLoader:
    def __init__(self):
        load_dotenv(REPO_ROOT / ".env")
        key = os.getenv("ERA5_CDS_API_KEY")
        if not key:
            raise ValueError("ERA5_CDS_API_KEY is missing in .env")
        self.client = cdsapi.Client(url=CDS_API_URL, key=key)

    def retrieve(self, dataset, request, target):
        return self.client.retrieve(dataset, request, str(target))


if __name__ == "__main__":
    data_format = "netcdf"
    variable = "geopotential" # random variable
    date = "2024-03-01" # random test date

    extension = "nc" if data_format == "netcdf" else "grib"
    target = REPO_ROOT / "data" / "era5" / "cache" / variable / f"era5_{date}.{extension}"
    target.parent.mkdir(parents=True, exist_ok=True)

    request = {
        "product_type": ["reanalysis"],
        "variable": [variable],
        "year": ["2024"],
        "month": ["03"],
        "day": ["01"],
        "time": ["13:00"],
        "pressure_level": ["550"],
        "data_format": data_format,
    }
    if data_format == "netcdf":
        request["download_format"] = "unarchived"

    loader = Era5DataLoader()
    print(f"Downloading ({data_format}) → {target}")
    loader.retrieve("reanalysis-era5-pressure-levels", request, target)
