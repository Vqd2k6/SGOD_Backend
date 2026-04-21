"""
app/routers/contact.py — API endpoint for Contact Form submissions.

Routes:
    POST /api/contact   → Submit a contact form
"""
import logging

from fastapi import APIRouter

from app.schemas.common import ApiResponse
from app.schemas.contact import ContactFormRequest, ContactFormResponse
from app.services import contact_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["Contact"])


@router.post(
    "/contact",
    response_model=ApiResponse[ContactFormResponse],
    status_code=201,
    summary="Gửi form liên hệ",
)
def submit_contact_form(payload: ContactFormRequest) -> ApiResponse[ContactFormResponse]:
    """
    Accept and validate a contact form submission.

    Pydantic automatically returns HTTP 422 with field-level error details
    if any validation rule fails (e-mail format, required fields, etc.).
    """
    logger.info("POST /api/contact ← %r <%s>", payload.name, payload.email)
    result = contact_service.handle_contact_submission(payload)
    return ApiResponse(data=result)
