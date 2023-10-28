from fastapi import APIRouter


carshop_router = APIRouter(prefix='/car-shop', tags=['Cars for sale'])


from carshop import carshop_api