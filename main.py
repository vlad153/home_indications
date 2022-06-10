from fastapi import FastAPI

from home_indication.router.route import image_router

api = FastAPI()


api.include_router(image_router, tags=['recognition'])