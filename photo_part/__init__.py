from fastapi import APIRouter, UploadFile


photo_router = APIRouter(prefix='/photo', tags=['Photos'])

from photo_part import photo_partapi