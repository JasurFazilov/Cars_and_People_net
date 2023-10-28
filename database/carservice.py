from database.models import UserCar
from database import get_db


def get_all_user_cars_db(user_id):
    db = next(get_db())

    all_cars = db.query(UserCar).filter_by(user_id=user_id).all()

    return all_cars


def get_exact_user_car_db(user_id, car_id):
    db = next(get_db())

    exact_user_car = db.query(UserCar).filter_by(user_id=user_id, car_id=car_id).first()

    if exact_user_car:
        return exact_user_car

    return False


def add_user_car_db(user_id, car_brand, car_model, car_model_year, car_model_color, car_trans, reg_date):
    db = next(get_db())

    new_car = UserCar(user_id=user_id, car_brand=car_brand, car_model=car_model, car_model_year=car_model_year,
                      car_model_color=car_model_color, car_trans=car_trans, reg_date=reg_date)

    db.add(new_car)
    db.commit()

    return new_car.car_id


def edit_user_car_db(car_id, edit_info, new_info):
    db = next(get_db())

    exact_user_car = db.query(UserCar).filter_by(car_id=car_id).first()

    if exact_user_car:
        if edit_info == 'car_brand':
            exact_user_car.car_brand = new_info

        elif edit_info == 'car_model':
            exact_user_car.car_model = new_info

        elif edit_info == 'car_model_year':
            exact_user_car.car_model_year = new_info

        elif edit_info == 'car_model_color':
            exact_user_car.car_model_color = new_info

        elif edit_info == 'car_trans':
            exact_user_car.car_trans = new_info

        db.commit()

        return 'Changes applied successfully'

    return 'Car not found'


def delete_car_db(car_id):
    db = next(get_db())

    exact_car = db.query(UserCar).filter_by(car_id=car_id).first()

    if exact_car:
        db.delete(exact_car)
        db.commit()

        return 'Car deleted'

    return 'Car not found'


def upload_car_photo_db(car_id, photo_path):
    db = next(get_db())

    exact_car = db.query(UserCar).filter_by(car_id=car_id).first()

    if exact_car:
        exact_car.car_photo = photo_path
        db.commit()

        return 'Car photo added'

    return 'Car not found'


def delete_car_photo_db(car_id):
    db = next(get_db())

    exact_car = db.query(UserCar).filter_by(car_id=car_id).first()

    if exact_car:
        exact_car.car_photo = 'None'
        db.commit()

        return 'Car photo deleted'

    return 'Car not found'

