from fastapi import APIRouter


car_router = APIRouter(prefix='/car', tags=['User cars'])

from cars import cars_api