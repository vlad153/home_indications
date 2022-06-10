import numpy as np 
from fastapi import APIRouter, File

import cv2 as cv
import pytesseract

image_router = APIRouter()

@image_router.post('/image')
async def recognize_image(file: bytes = File()):
    nparr = np.fromfile(file, np.uint8)
    img_np = cv.imdecode(nparr, cv.IMREAD_COLOR)
    return img_np