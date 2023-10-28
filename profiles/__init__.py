from fastapi import APIRouter


profiles_router = APIRouter(prefix='/profile', tags=['Profiles'])

from profiles import profiles_api