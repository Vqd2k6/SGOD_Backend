"""
app/routers/news.py — API endpoints for News Slider and Blog Posts.

Routes:
    GET  /api/news              → All news slider items
    GET  /api/blog              → All blog posts (supports ?category=&search=)
    GET  /api/blog/{id}         → Single blog post detail
"""
import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, Query

from app.schemas.common import ApiResponse
from app.schemas.news import BlogPost, NewsSlide
from app.services import news_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api", tags=["News & Blog"])


@router.get(
    "/news",
    response_model=ApiResponse[list[NewsSlide]],
    summary="Lấy danh sách tin tức slider",
)
def list_news_slides() -> ApiResponse[list[NewsSlide]]:
    """Return all news carousel slides."""
    slides = news_service.get_all_news_slides()
    logger.debug("GET /api/news → %d slides", len(slides))
    return ApiResponse(data=slides)


@router.get(
    "/blog",
    response_model=ApiResponse[list[BlogPost]],
    summary="Lấy danh sách bài viết (có thể lọc)",
)
def list_blog_posts(
    category: Optional[str] = Query(default=None, description="Lọc theo danh mục: AI | Blockchain | Security"),
    search: Optional[str] = Query(default=None, description="Tìm kiếm theo tiêu đề bài viết"),
) -> ApiResponse[list[BlogPost]]:
    """
    Return blog posts, optionally filtered by category and/or full-text search.

    Examples:
        GET /api/blog
        GET /api/blog?category=AI
        GET /api/blog?search=blockchain&category=Blockchain
    """
    posts = news_service.get_all_blog_posts(category=category, search=search)
    logger.debug("GET /api/blog (category=%r, search=%r) → %d posts", category, search, len(posts))
    return ApiResponse(data=posts)


@router.get(
    "/blog/{post_id}",
    response_model=ApiResponse[BlogPost],
    summary="Lấy chi tiết một bài viết",
)
def get_blog_post(post_id: int) -> ApiResponse[BlogPost]:
    """
    Return a single blog post by its integer ID.

    Raises:
        HTTPException 404: If the post does not exist.
    """
    post = news_service.get_blog_post_by_id(post_id)
    if post is None:
        logger.warning("GET /api/blog/%d → 404 Not Found", post_id)
        raise HTTPException(status_code=404, detail=f"Không tìm thấy bài viết với id={post_id}")
    return ApiResponse(data=post)
