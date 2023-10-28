from database.models import User
from database import get_db


def get_all_users_db():
    db = next(get_db())

    all_users = db.query(User).all()

    return all_users


def get_exact_user_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        return exact_user

    return False


def add_new_user_db(name, surname, email, password, city, birthday, reg_date):
    db = next(get_db())

    checker = db.query(User).filter_by(email=email).first()

    if checker:
        return 'This email is already registered'

    else:
        new_user = User(name=name, surname=surname, email=email, password=password, city=city, birthday=birthday,
                        reg_date=reg_date)

        db.add(new_user)
        db.commit()

        return 'User registered'


def login_user_db(email, password):
    db = next(get_db())

    user = db.query(User).filter_by(email=email, password=password).first()

    if user:
        return user

    return 'Registration error'


def edit_user_info_db(user_id, edit_info, new_info):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        if edit_info == 'city':
            exact_user.city = new_info

        elif edit_info == 'email':
            exact_user.email = new_info

        elif edit_info == 'password':
            exact_user.password = new_info

        elif edit_info == 'name':
            exact_user.name = new_info

        elif edit_info == 'surname':
            exact_user.surname = new_info

        db.commit()

        return 'Changes applied successfully'

    return 'User not found'


def delete_user_db(user_id):
    db = next(get_db())

    user = db.query(User).filter_by(user_id=user_id).first()

    if user:
        db.delete(user)
        db.commit()

        return 'User deleted'

    return 'User not found'


def upload_profile_photo_db(user_id, photo_path):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = photo_path
        db.commit()

        return 'Profile photo added'

    return 'User not found'


def delete_profile_photo_db(user_id):
    db = next(get_db())

    exact_user = db.query(User).filter_by(user_id=user_id).first()

    if exact_user:
        exact_user.profile_photo = 'None'
        db.commit()

        return 'Profile photo deleted'

    return 'User not found'
