"""
app/schemas/news.py — Pydantic models for the News Slider & Blog endpoints.
"""
from typing import Optional

from pydantic import BaseModel


class NewsSlide(BaseModel):
    """Represents a single slide in the news carousel."""

    id: int
    title: str
    description: str
    image: str          # URL validated as string for flexibility with external CDNs
    color: str          # Tailwind gradient class string


class BlogPost(BaseModel):
    """Represents a single blog article."""

    id: int
    title: str
    description: str
    author: str
    date: str           # ISO-8601 date string, e.g. "2024-09-10"
    views: int
    image: str
    category: str
    featured: bool = False
    readTime: Optional[int] = None
