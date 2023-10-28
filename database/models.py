from sqlalchemy import Integer, DateTime, Date, Column, String, ForeignKey, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String)
    surname = Column(String)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    city = Column(String)
    birthday = Column(Date)
    profile_photo = Column(String)

    reg_date = Column(DateTime)


class UserPost(Base):
    __tablename__ = 'user_posts'
    post_id = Column(Integer, autoincrement=True, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_text = Column(String)
    likes = Column(Integer, default=0)

    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')


class PostPhoto(Base):
    __tablename__ = 'post_photos'
    photo_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    car_id = Column(Integer, ForeignKey('user_cars.car_id'))
    photo_path = Column(String)

    post_fk = relationship(UserPost, lazy='subquery')



class PostComment(Base):
    __tablename__ = 'post_comments'
    comment_id = Column(Integer, autoincrement=True, primary_key=True)
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))
    car_id = Column(Integer, ForeignKey('user_cars.car_id'))


    comment_text = Column(String)
    publish_date = Column(DateTime)

    user_fk = relationship(User, lazy='subquery')
    post_fk = relationship(UserPost, lazy='subquery')


class UserCar(Base):
    __tablename__ = 'user_cars'
    car_id = Column(Integer, autoincrement=True, primary_key=True)
    car_brand = Column(String)
    car_model = Column(String)
    car_model_year = Column(String)
    car_model_color = Column(String)
    car_trans = Column(String)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    post_id = Column(Integer, ForeignKey('user_posts.post_id'))
    photo_id = Column(Integer, ForeignKey('post_photos.photo_id'))

    user_fk = relationship(User, lazy='subquery', foreign_keys=[user_id])
    post_fk = relationship(UserPost, lazy='subquery', foreign_keys=[post_id])
    photo_fk = relationship(PostPhoto, lazy='subquery', foreign_keys=[photo_id])

    reg_date = Column(DateTime)


class CarProductShop(Base):
    __tablename__ = 'product_shop'
    product_id = Column(Integer, autoincrement=True, primary_key=True)
    product_name = Column(String)
    product_price = Column(Float)
    product_describe = Column(String)
    product_qty = Column(Integer)
    car_id = Column(Integer, ForeignKey('user_cars.car_id'))

    car_fk = relationship(UserCar, lazy='subquery')



class CarShop(Base):
    __tablename__ = 'car_sale'
    sale_car_id = Column(Integer, autoincrement=True, primary_key=True)
    car_price = Column(Float)
    contacts = Column(String)
    car_id = Column(Integer, ForeignKey('user_cars.car_id'))
    user_id = Column(Integer, ForeignKey('users.user_id'))

    car_fk = relationship(UserCar, lazy='subquery')
    user_fk = relationship(User, lazy='subquery')
