"""
app/schemas/contact.py — Pydantic models for the Contact Form endpoint.
"""
from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator


class ContactFormRequest(BaseModel):
    """Incoming contact form payload — all fields are validated by Pydantic."""

    name: str
    email: EmailStr          # Pydantic validates e-mail format automatically
    phone: Optional[str] = None
    subject: str
    message: str

    @field_validator("name")
    @classmethod
    def name_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Họ tên không được để trống.")
        return value.strip()

    @field_validator("subject")
    @classmethod
    def subject_must_not_be_blank(cls, value: str) -> str:
        if not value.strip():
            raise ValueError("Tiêu đề không được để trống.")
        return value.strip()

    @field_validator("message")
    @classmethod
    def message_min_length(cls, value: str) -> str:
        if len(value.strip()) < 10:
            raise ValueError("Nội dung phải có ít nhất 10 ký tự.")
        return value.strip()


class ContactFormResponse(BaseModel):
    """Response returned after successfully receiving a contact submission."""

    message: str
    received_name: str
    received_email: str
