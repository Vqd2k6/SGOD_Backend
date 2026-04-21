"""
app/schemas/team.py — Pydantic models for Team Member endpoint.
"""
from pydantic import BaseModel


class SocialLinks(BaseModel):
    """Social media URLs for a team member."""

    facebook: str = "#"
    twitter: str = "#"
    instagram: str = "#"
    linkedin: str = "#"
    reddit: str = "#"


class TeamMember(BaseModel):
    """Represents a single member of the SGOD team."""

    id: int
    name: str
    title: str
    position: str
    department: str
    bio: str
    birthYear: int
    detailedBio: list[str]
    imageURL: str
    socialLinks: SocialLinks
