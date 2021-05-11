from pathlib import Path
from django.core.management.utils import get_random_secret_key

BASE_DIR = Path(__file__).resolve().parent.parent

# secret key is generated
SECRET_KEY = get_random_secret_key()

# put your database settings below, or leave default to create sqlite db
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# fill in your gmail address and password
EMAIL_HOST_USER = '@gmail.com'
EMAIL_HOST_PASSWORD = ''

# fill in the url address, where the project is hosted.
# Default django development server at http://127.0.0.1:8000
BASE_URL = 'http://127.0.0.1:8000'
