"""
app/services/contact_service.py — Business logic for Contact Form submissions.

In a production system this layer would:
  - Persist the submission to a database.
  - Send a notification e-mail via an SMTP / transactional-email provider.
For now it logs the payload and returns a success acknowledgement.
"""
import logging

from app.schemas.contact import ContactFormRequest, ContactFormResponse

logger = logging.getLogger(__name__)


def handle_contact_submission(payload: ContactFormRequest) -> ContactFormResponse:
    """
    Process an incoming contact form submission.

    Args:
        payload: Validated ContactFormRequest data.

    Returns:
        ContactFormResponse acknowledging receipt.
    """
    # TODO: Replace with DB persist + e-mail dispatch in production.
    logger.info(
        "New contact submission — name=%r | email=%r | subject=%r",
        payload.name,
        payload.email,
        payload.subject,
    )

    return ContactFormResponse(
        message="Cảm ơn bạn đã liên hệ! Chúng tôi sẽ phản hồi trong vòng 24 giờ.",
        received_name=payload.name,
        received_email=payload.email,
    )
