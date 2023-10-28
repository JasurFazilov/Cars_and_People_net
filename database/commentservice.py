from database.models import PostComment
from database import get_db


def get_exact_post_comment_db(post_id):
    db = next(get_db())

    exact_post_comment = db.query(PostComment).filter_by(post_id=post_id).all()

    if exact_post_comment:
        return exact_post_comment
    return 'Commentary not found'


def add_new_comment_db(post_id, user_id, car_id, comment_text, publish_date):
    db = next(get_db())

    new_comment = PostComment(post_id=post_id, user_id=user_id, car_id=car_id, comment_text=comment_text, publish_date=publish_date)

    db.add(new_comment)
    db.commit()

    return 'Commentary added'


def change_exact_comment_db(comment_id, new_comment_text, publish_date):
    db = next(get_db())

    exact_post_comment = db.query(PostComment).filter_by(comment_id=comment_id, publish_date=publish_date).first()

    if exact_post_comment:
        exact_post_comment.new_comment = new_comment_text
        db.commit()

        return 'Commentary edited'
    return 'Commentary found'


def delete_exact_comment_db(comment_id):
    db = next(get_db())

    exact_comment = db.query(PostComment).filter_by(comment_id=comment_id).first()

    if exact_comment:
        db.delete(exact_comment)
        db.commit()

        return 'Commentary deleted'

    return 'Commentary found'

