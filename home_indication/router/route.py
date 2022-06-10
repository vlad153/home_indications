import numpy as np 
from fastapi import APIRouter, File

import cv2 as cv
import pytesseract

image_router = APIRouter()

@image_router.post('/image')
async def recognize_image(file: bytes = File()):
    image_array = np.asarray(bytearray(file), dtype="uint8")
    image = cv.imdecode(image_array, cv.IMREAD_COLOR)
    data_image = pytesseract.image_to_data(image)
    return data_image