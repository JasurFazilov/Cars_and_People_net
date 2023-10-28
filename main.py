from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from registration import user_router
from cars.cars_api import car_router
from comments.comment_api import comment_router
from photo_part.photo_partapi import photo_router
from posts.post_api import posts_router
from profiles.profiles_api import profiles_router
from carshop.carshop_api import carshop_router


from database import Base, engine


Base.metadata.create_all(bind=engine)


app = FastAPI(docs_url='/')

app.mount(path='/gallery', app=StaticFiles(directory='media'))


app.include_router(user_router)
app.include_router(car_router)
app.include_router(comment_router)
app.include_router(photo_router)
app.include_router(posts_router)
app.include_router(profiles_router)
app.include_router(carshop_router)