"""
app/routers/team.py — API endpoints for Team Members.

Routes:
    GET  /api/team          → All team members
    GET  /api/team/{id}     → Single team member detail
"""
import logging

from fastapi import APIRouter, HTTPException

from app.schemas.common import ApiResponse
from app.schemas.team import TeamMember
from app.services import team_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["Team"])


@router.get(
    "/team",
    response_model=ApiResponse[list[TeamMember]],
    summary="Lấy danh sách đội ngũ nhân sự",
)
def list_team_members() -> ApiResponse[list[TeamMember]]:
    """Return all SGOD team members."""
    members = team_service.get_all_team_members()
    logger.debug("GET /api/team → %d members", len(members))
    return ApiResponse(data=members)


@router.get(
    "/team/{member_id}",
    response_model=ApiResponse[TeamMember],
    summary="Lấy thông tin chi tiết một thành viên",
)
def get_team_member(member_id: int) -> ApiResponse[TeamMember]:
    """
    Return a single team member by ID.

    Raises:
        HTTPException 404: If the member does not exist.
    """
    member = team_service.get_team_member_by_id(member_id)
    if member is None:
        logger.warning("GET /api/team/%d → 404 Not Found", member_id)
        raise HTTPException(status_code=404, detail=f"Không tìm thấy thành viên với id={member_id}")
    return ApiResponse(data=member)
