from fastapi import FastAPI

from home_indication.router.route import image_router

app = FastAPI()


app.include_router(image_router, tags=['recognition'])