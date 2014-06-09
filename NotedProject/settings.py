import os;
BASE_DIR = os.path.dirname(os.path.dirname(__file__));
SETTINGS_DIR = os.path.dirname(__file__);
PROJECT_PATH = os.path.abspath(os.path.join(SETTINGS_DIR, os.pardir));



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "-ecect6^rd_#xndb0(efo^z*yv*$b2tm*gd%vry+-jgbr9$&rm";

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True;

TEMPLATE_DEBUG = True;

ALLOWED_HOSTS = ["dr01d3k4.pythonanywhere.com"];



INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "noted"
);

MIDDLEWARE_CLASSES = (
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
);



ROOT_URLCONF = "NotedProject.urls";

WSGI_APPLICATION = "NotedProject.wsgi.application";



DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "noted.sqlite3"),
    }
}



LANGUAGE_CODE = "en-us";

TIME_ZONE = "UTC";

USE_I18N = True;

USE_L10N = True;

USE_TZ = True;



STATIC_PATH = os.path.join(PROJECT_PATH, "static");
STATIC_URL = "/static/";
STATICFILES_DIRS = (
    STATIC_PATH,
);

TEMPLATE_PATH = os.path.join(PROJECT_PATH, "templates");
TEMPLATE_DIRS = (
    TEMPLATE_PATH,
);

MEDIA_URL = "/media/";
MEDIA_ROOT = os.path.join(PROJECT_PATH, "media");