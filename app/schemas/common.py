"""
app/schemas/common.py — Shared response envelope used by every endpoint.

All API responses follow the structure:
    { "success": true, "data": <payload> }
or on error:
    { "success": false, "error": "<message>" }
"""
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ApiResponse(BaseModel, Generic[T]):
    """Generic success envelope."""

    success: bool = True
    data: T


class ApiError(BaseModel):
    """Generic error envelope."""

    success: bool = False
    error: str
