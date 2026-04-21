"""
app/services/news_service.py — Business logic for News Slider & Blog.

Reads JSON files once at import time and exposes pure-function helpers
so the router layer stays thin (no direct I/O or filtering logic there).
"""
import json
import logging
from pathlib import Path
from typing import Optional

from app.schemas.news import BlogPost, NewsSlide

logger = logging.getLogger(__name__)

# ── Load data at startup (fast, no DB round-trip needed for JSON-based MVP) ──
_DATA_DIR = Path(__file__).parent.parent / "data"


def _load_json(filename: str) -> list[dict]:
    """Read and parse a JSON file from the data directory."""
    filepath = _DATA_DIR / filename
    with filepath.open(encoding="utf-8") as fh:
        return json.load(fh)


_news_slides_raw: list[dict] = _load_json("news.json")
_blog_posts_raw: list[dict] = _load_json("blog.json")

# Pre-validate all records into Pydantic models once
_news_slides: list[NewsSlide] = [NewsSlide(**item) for item in _news_slides_raw]
_blog_posts: list[BlogPost] = [BlogPost(**item) for item in _blog_posts_raw]

logger.info(
    "Loaded %d news slides and %d blog posts from JSON.",
    len(_news_slides),
    len(_blog_posts),
)


# ─────────────────────────────────────────────
# Public service functions
# ─────────────────────────────────────────────

def get_all_news_slides() -> list[NewsSlide]:
    """Return the full list of news slider items."""
    return _news_slides


def get_all_blog_posts(
    category: Optional[str] = None,
    search: Optional[str] = None,
) -> list[BlogPost]:
    """
    Return blog posts optionally filtered by category and/or search query.

    Args:
        category: Exact category name to filter by (case-insensitive).
        search:   Substring to search for within the post title (case-insensitive).

    Returns:
        Filtered and sorted list of BlogPost models.
    """
    results = _blog_posts

    if category:
        results = [p for p in results if p.category.lower() == category.lower()]

    if search:
        query = search.lower()
        results = [p for p in results if query in p.title.lower()]

    # Default sort: newest first
    results = sorted(results, key=lambda p: p.date, reverse=True)
    logger.debug(
        "get_all_blog_posts(category=%r, search=%r) → %d results",
        category,
        search,
        len(results),
    )
    return results


def get_blog_post_by_id(post_id: int) -> Optional[BlogPost]:
    """
    Look up a single blog post by its unique ID.

    Returns:
        BlogPost if found, otherwise None.
    """
    return next((p for p in _blog_posts if p.id == post_id), None)
