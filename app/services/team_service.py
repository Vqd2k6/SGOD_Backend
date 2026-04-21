"""
app/services/team_service.py — Business logic for the Team endpoint.
"""
import json
import logging
from pathlib import Path
from typing import Optional

from app.schemas.team import TeamMember

logger = logging.getLogger(__name__)

_DATA_DIR = Path(__file__).parent.parent / "data"

_team_raw: list[dict] = json.loads((_DATA_DIR / "team.json").read_text(encoding="utf-8"))
_team_members: list[TeamMember] = [TeamMember(**m) for m in _team_raw]

logger.info("Loaded %d team members from JSON.", len(_team_members))


def get_all_team_members() -> list[TeamMember]:
    """Return the complete list of team members."""
    return _team_members


def get_team_member_by_id(member_id: int) -> Optional[TeamMember]:
    """Return a single team member by ID, or None if not found."""
    return next((m for m in _team_members if m.id == member_id), None)
