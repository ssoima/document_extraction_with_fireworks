import base64
import os
from io import BytesIO

import cv2
import numpy as np
from PIL.ImageFile import ImageFile
from PIL import Image, ImageEnhance
from dotenv import load_dotenv

load_dotenv()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


def binary_stream_to_base64(image: ImageFile) -> str:
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")


FIREWORKS_API_KEY: str = os.getenv("FIREWORKS_API_KEY")

if FIREWORKS_API_KEY is None:
    raise ValueError("FIREWORKS_API_KEY is not set in the environment variables.")
