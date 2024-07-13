import json
import os

import cloudinary
from cloudinary import uploader
from cloudinary.utils import cloudinary_url
from distinctid import distinct

URL = "http://127.0.0.1:9500"

# Configuration
cloudinary.config(
    cloud_name=os.getenv("CLOUD_NAME"),
    api_key=os.getenv("API_KEY"),
    api_secret=os.getenv("API_SECRET"),
    upload_prefix=URL,
    secure=True,
)


# python3 investigate.py | python3 -m json.tool
print(
    json.dumps(
        cloudinary.Search()
        .expression("pyconng2024")
        .sort_by("public_id", "asc")
        .max_results("100")
        .execute()
    )
)
