from fastapi import APIRouter


comment_router = APIRouter(prefix='/comments', tags=['Comments to post'])

from comments import comment_api