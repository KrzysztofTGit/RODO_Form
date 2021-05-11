from pathlib import Path
from django.template.backends import django
try:
    from RODO_Form import dev_settings as sett
except ImportError:
    try:
        from RODO_Form import local_settings as sett
    except ImportError:
        print("Nie znaleziono pliku 'local_settings.py' w folderze 'RODO_Form!'")
        exit(0)

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rodo_app'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'RODO_Form.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'RODO_Form.wsgi.application'

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

try:
    from RODO_Form.dev_settings import DATABASES
    print("Dev imported")
except ImportError:
    try:
        from RODO_Form.local_settings import DATABASES
        print("local imported")
    except ModuleNotFoundError:
        print("Brak konfiguracji bazy danych w pliku local_settings.py!")
        print("Uzupełnij dane i spróbuj ponownie!")
        exit(0)

try:
    from RODO_Form.dev_settings import SECRET_KEY
    print("Dev imported")
except ImportError:
    try:
        from RODO_Form.local_settings import SECRET_KEY
        print("local imported")
    except ModuleNotFoundError:
        print("Brak SECRET_KEY w pliku local_settings.py!")
        print("Uzupełnij dane i spróbuj ponownie!")
        exit(0)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = sett.EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = sett.EMAIL_HOST_PASSWORD
EMAIL_USE_SSL = False

BASE_URL = sett.BASE_URL
