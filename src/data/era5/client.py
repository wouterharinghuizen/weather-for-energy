import cdsapi
import os
from pathlib import Path
from dotenv import load_dotenv

CDS_API_URL = "https://cds.climate.copernicus.eu/api"
REPO_ROOT = Path(__file__).resolve().parents[3]


class Era5DataLoader:
    def __init__(self, api_key: str | None = None):
        load_dotenv(REPO_ROOT / ".env")
        key = api_key or os.getenv("ERA5_CDS_API_KEY")
        if not key:
            raise ValueError(
                "ERA5_CDS_API_KEY is missing in .env"
            )
        self.client = cdsapi.Client(url=CDS_API_URL, key=key)

    def retrieve(self, dataset: str, request: dict, target: str | Path):
        return self.client.retrieve(dataset, request, str(target))


if __name__ == "__main__":
    loader = Era5DataLoader()
    loader.retrieve(
        dataset="reanalysis-era5-pressure-levels",
        request={
            "product_type": ["reanalysis"],
            "variable": ["geopotential"],
            "year": ["2024"],
            "month": ["03"],
            "day": ["01"],
            "time": ["13:00"],
            "pressure_level": ["550"],
            "data_format": "grib",
        },
        target=REPO_ROOT / "data/era5/example.grib",
    )
