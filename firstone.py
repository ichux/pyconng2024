import json
import os

import cloudinary
from cloudinary import uploader
from cloudinary.utils import cloudinary_url
from distinctid import distinct

# Configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET"),
    upload_prefix="https://api.cloudinary.com",
    secure=True,
)


response = uploader.upload("flyer.jpeg", tags="pyconng2024", public_id=distinct())
print(json.dumps(response, indent=1))
