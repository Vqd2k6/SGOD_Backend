"""
app/routers/company.py — API endpoints for Company Information.

Routes:
    GET /api/company/vision
    GET /api/company/mission
    GET /api/company/products
    GET /api/company/contact-info
"""
import logging

from fastapi import APIRouter

from app.schemas.common import ApiResponse
from app.schemas.company import ContactInfoData, VisionMissionData
from app.services import company_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/company", tags=["Company Data"])

@router.get("/vision", response_model=ApiResponse[VisionMissionData], summary="Lấy dữ liệu Tầm nhìn")
def get_vision() -> ApiResponse[VisionMissionData]:
    data = company_service.get_vision()
    return ApiResponse(data=data)

@router.get("/mission", response_model=ApiResponse[VisionMissionData], summary="Lấy dữ liệu Sứ mệnh")
def get_mission() -> ApiResponse[VisionMissionData]:
    data = company_service.get_mission()
    return ApiResponse(data=data)

@router.get("/products", response_model=ApiResponse[list[str]], summary="Lấy dữ liệu Sản phẩm")
def get_products() -> ApiResponse[list[str]]:
    data = company_service.get_products()
    return ApiResponse(data=data)

@router.get("/contact-info", response_model=ApiResponse[ContactInfoData], summary="Lấy thông tin liên hệ công ty")
def get_contact_info() -> ApiResponse[ContactInfoData]:
    data = company_service.get_contact_info()
    return ApiResponse(data=data)
