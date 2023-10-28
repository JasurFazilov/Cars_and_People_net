from fastapi import APIRouter
from pydantic import BaseModel
from datetime import datetime, date

user_router = APIRouter(prefix='/user', tags=['User'])


class RegisterModel(BaseModel):
    name: str
    surname: str
    email: str
    password: str
    city: str
    birthday: date
    reg_date: datetime = datetime.now()


class LoginModel(BaseModel):
    email: str
    password: str


from registration import registration_api
