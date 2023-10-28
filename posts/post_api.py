from fastapi import Body
from datetime import datetime

from posts import posts_router
from database.postservice import (add_new_post_db, delete_post_db, edit_post_text_db,
                                  get_exact_post_db, get_all_posts_db, like_post_db, unlike_post_db)


@posts_router.get('/all-posts')
async def all_posts():
    result = get_all_posts_db()

    return {'status': 1, 'message': result}


@posts_router.get('/get-exact-post')
async def exact_post(post_id: int):
    result = get_exact_post_db(post_id)

    if result:
        return {'status': 1, 'message': result}

    else:
        return {'status': 0, 'message': 'Post not found'}


@posts_router.delete('/delete-post')
async def delete_post(post_id: int):
    result = delete_post_db(post_id)

    return {'status': 1, 'message': result}


@posts_router.put('/edit-post')
async def edit_post(post_id: int = Body(...), new_text: str = Body(...)):
    result = edit_post_text_db(post_id=post_id, new_text=new_text)

    return {'status': 1, 'message': result}


@posts_router.post('/post-like')
async def like_post(post_id: int):
    result = like_post_db(post_id)

    return {'status': 1, 'message': result}


@posts_router.put('/unlike-post')
async def unlike_post(post_id: int):
    result = unlike_post_db(post_id)

    return {'status': 1, 'message': result}


@posts_router.post('/new-post')
async def new_post(user_id: int = Body(...), post_text: str = Body(...)):
    result = add_new_post_db(user_id=user_id, post_text=post_text, publish_date=datetime.now())

    return {'status': 1, 'message': result}
