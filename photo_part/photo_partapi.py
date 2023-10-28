from fastapi import UploadFile

from photo_part import photo_router
from database.postservice import upload_post_photo_db
from database.carservice import upload_car_photo_db


@photo_router.post('/post-photo')
async def post_photo_upload(post_id: int, photo_path: UploadFile):
    with open(f'/media/{photo_path.filename}', 'wb') as file:
        post_photo = await photo_path.read()
        file.write(post_photo)

    result = upload_post_photo_db(post_id, f'/gallery/{photo_path.filename}')

    return {'status': 1, 'message': result}


@photo_router.post('/post-car-photo')
async def upload_car_photo(car_id: int, photo_path: UploadFile):
    with open(f'/media/{photo_path.filename}', 'wb') as file:
        post_photo = await photo_path.read()
        file.write(post_photo)

    result = upload_car_photo_db(car_id, f'/gallery/{photo_path.filename}')

    return {'status': 1, 'message': result}



@photo_router.post('/sale-car-photo')
async def upload_sale_car_photo_db(sale_car_id: int, photo_path: UploadFile):
    with open(f'/media/{photo_path.filename}', 'wb') as file:
        post_photo = await photo_path.read()
        file.write(post_photo)

    result = upload_car_photo_db(sale_car_id, f'/gallery/{photo_path.filename}')

    return {'status': 1, 'message': result}
