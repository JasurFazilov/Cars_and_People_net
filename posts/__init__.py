from fastapi import APIRouter

posts_router = APIRouter(prefix='/posts', tags=['Posts'])

from posts import post_api
