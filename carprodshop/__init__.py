from fastapi import APIRouter

shop_router = APIRouter(prefix='/cars-products-shop', tags=['Shop'])

from carprodshop import carprodshop_api
