
from pathlib import Path
import os 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '$ku-7=zril351boce5l0=0ra0vg5^+*j^a657c!a*$hsco2mte'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}