"""
app/services/company_service.py — Business logic for Company info endpoints.
"""
import json
import logging
from pathlib import Path

from app.schemas.company import ContactInfoData, VisionMissionData

logger = logging.getLogger(__name__)

_DATA_DIR = Path(__file__).parent.parent / "data"

def _load_json(filename: str) -> dict | list:
    """Read and parse a JSON file from the data directory."""
    filepath = _DATA_DIR / filename
    with filepath.open(encoding="utf-8") as fh:
        return json.load(fh)

_vision_raw = _load_json("vision.json")
_mission_raw = _load_json("mission.json")
_products_raw = _load_json("products.json")
_contact_info_raw = _load_json("contact_info.json")

_vision_data = VisionMissionData(**_vision_raw)
_mission_data = VisionMissionData(**_mission_raw)
_products_data = list(_products_raw)
_contact_info_data = ContactInfoData(**_contact_info_raw)

logger.info("Loaded company info (vision, mission, products, contact_info) from JSON.")

def get_vision() -> VisionMissionData:
    return _vision_data

def get_mission() -> VisionMissionData:
    return _mission_data

def get_products() -> list[str]:
    return _products_data

def get_contact_info() -> ContactInfoData:
    return _contact_info_data
