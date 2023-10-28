from fastapi import Body, UploadFile
from datetime import datetime


from carshop import carshop_router
from database.carshopservice import add_car_sale_db, get_exact_sale_car_db, delete_exact_sell_car_db, upload_sale_car_photo_db


@carshop_router.post('/add-car-sale')
async def add_car_sale(car_id, car_price, user_id, contacts):
    result = add_car_sale_db(car_id, user_id, car_price, contacts)

    return {'status': 1, 'message': result}


@carshop_router.get('/exact-car-sale')
async def get_exact_sale_car(sale_car_id):
    result = get_exact_sale_car_db(sale_car_id)

    return {'status': 1, 'message': result}


@carshop_router.delete('/delete-sale-car')
async def delete_sale_car(sale_car_id):
    result = delete_exact_sell_car_db(sale_car_id)

    return {'status': 1, 'message': result}


