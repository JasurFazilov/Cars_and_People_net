from fastapi import Body, UploadFile
from datetime import datetime

from cars import car_router
from database.carservice import (get_all_user_cars_db, get_exact_user_car_db, add_user_car_db,
                                 edit_user_car_db, delete_car_db, upload_car_photo_db, delete_car_photo_db)


@car_router.get('/get-user-all-cars')
async def get_all_user_cars(user_id: int):
    result = get_all_user_cars_db(user_id)

    return {'status': 1, 'message': result }


@car_router.get('/get-exact-user-car')
async def get_exact_user_car(user_id: int, car_id: int):
    result = get_exact_user_car_db(car_id, user_id)

    if result:
        return {'status': 1, 'message': result}

    else:
        return {'status': 0, 'message': 'Car not found'}


@car_router.post('/add-user-car')
async def add_user_car(user_id: int = Body(...), car_brand: str = Body(...), car_model: str = Body(...),
                       car_model_year: int = Body(...), car_model_color: str = Body(...), car_trans: str = Body(...) ):
    result = add_user_car_db(user_id=user_id, car_brand=car_brand, car_model=car_model,
                             car_model_year=car_model_year, car_model_color=car_model_color, car_trans=car_trans,
                             reg_date=datetime.now())

    return {'status': 1, 'message': result}


@car_router.put('/edit-user-car')
async def edit_user_car(car_id: int = Body(...), new_info: str = Body(...), edit_info: str = Body(...)):
    result = edit_user_car_db(car_id=car_id, edit_info=edit_info, new_info=new_info)

    return {'status': 1, 'message': result}


@car_router.delete('/user-car-delete')
async def delete_user_car(car_id: int):
    result = delete_car_db(car_id)

    return {'status': 1, 'message': result}


@car_router.post('/user-car-photo')
async def upload_car_photo(car_id: int, photo: UploadFile):
    with open(f'media/{photo.filename}', 'wb') as file:
        front_photo = await photo.read()
        file.write(front_photo)

    result = upload_car_photo_db(car_id, f'/gallery/{photo.filename}')

    return {'status': 1, 'message': result}


@car_router.delete('/user-car-photo')
async def delete_car_photo(car_id: int):
    result = delete_car_photo_db(car_id)

    return {'status': 1, 'message': result}
