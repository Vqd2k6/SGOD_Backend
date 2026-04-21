"""
app/schemas/company.py — Pydantic models for Company info (Vision, Mission, Products, Contact Info).
"""
from typing import Optional
from pydantic import BaseModel


class VisionMissionData(BaseModel):
    badge: str
    title: str
    paragraph: str
    points: list[str]


class CompanyDetails(BaseModel):
    name: str
    shortName: str
    taxCode: str


class ContactInfoItem(BaseModel):
    id: str
    icon: str
    label: str
    content: str


class ContactInfoData(BaseModel):
    company: CompanyDetails
    info: list[ContactInfoItem]
