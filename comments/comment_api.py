from fastapi import Body
from datetime import datetime

from comments import comment_router
from database.commentservice import (get_exact_post_comment_db,
                                     add_new_comment_db, delete_exact_comment_db, change_exact_comment_db)


@comment_router.get('/exact-comment')
async def get_post_comment(post_id: int):
    result = get_exact_post_comment_db(post_id)

    return {'status': 1, 'message': result}


@comment_router.post('/new-comment')
async def add_new_comment(post_id: int = Body(...), user_id: int = Body(...), car_id: int = Body(...),
                          comment_text: str = Body(...)):
    result = add_new_comment_db(post_id=post_id, user_id=user_id, car_id=car_id,
                                comment_text=comment_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}


@comment_router.put('/edit-comment')
async def edit_comment(comment_id: int = Body(...), new_comment_text: str = Body(...)):
    result = change_exact_comment_db(comment_id, new_comment_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}


@comment_router.delete('/delete-comment')
async def delete_comment(comment_id: int):
    result = delete_exact_comment_db(comment_id)

    return {'status': 1, 'message': result}
