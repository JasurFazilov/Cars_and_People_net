from registration import user_router, RegisterModel, LoginModel
from database.userservice import add_new_user_db, login_user_db, delete_user_db


@user_router.post('/register-user')
async def register_user(data: RegisterModel):
    register_data = data.model_dump()
    result = add_new_user_db(**register_data)

    return {'status': 1, 'message': result}


@user_router.post('/login')
async def login_user(data: LoginModel):
    login_data = data.model_dump()
    result = login_user_db(**login_data)

    return {'status': 1, 'message': result}


@user_router.delete('/delete-user')
async def delete_user(user_id: int):
    result = delete_user_db(user_id)

    return {'status': 1, 'message': result}