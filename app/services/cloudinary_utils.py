import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.utils import cloudinary_url
import os
from dotenv import load_dotenv
load_dotenv()

# Configuration       
cloudinary.config( 
    cloud_name = "dijo5boln", 
    api_key = os.getenv('CLOUDINARY_API_KEY'), 
    api_secret=os.getenv('CLOUDINARY_API_SECRET'), # Click 'View API Keys' above to copy your API secret
    secure=True
)

def upload_file(file):
    result = cloudinary.uploader.upload(file)
    return result