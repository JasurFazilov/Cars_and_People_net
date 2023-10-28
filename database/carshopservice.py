from database.models import CarShop
from database import get_db


def add_car_sale_db(car_id, car_price, user_id, contacts):
    db = next(get_db())

    new_car_sale = CarShop(car_id=car_id, user_id=user_id, car_price=car_price, contacts=contacts)

    db.add(new_car_sale)
    db.commit()

    return new_car_sale.sale_car_id


def get_exact_sale_car_db(sale_car_id):
    db = next(get_db())

    exact_sale_car = db.query(CarShop).filter_by(sale_car_id=sale_car_id).first()

    if exact_sale_car:
        return exact_sale_car

    return False


def delete_exact_sell_car_db(sale_car_id):
    db = next(get_db())

    exact_car = db.query(CarShop).filter_by(sale_car_id=sale_car_id).first()

    if exact_car:
        db.delete(exact_car)
        db.commit()

        return 'Car deleted'

    return 'Car not found'


def upload_sale_car_photo_db(sale_car_id, photo_path):
    db = next(get_db())

    new_photo = CarShop(sale_car_id=sale_car_id, photo_path=photo_path)

    db.add(new_photo)
    db.commit()

    return 'Photo added'
