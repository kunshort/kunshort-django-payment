INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.contenttypes",
    "django.contrib.auth",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.staticfiles",
    "kunshort_payment",
]

STATIC_URL = "/static/"

ROOT_URLCONF = "dev_urls"

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    }
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.sqlite3",
    }
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

PROVIDERS = {
    "MTN_CAMEROON": "MTN_CAMEROON",
}

PAYMENT_PROVIDER = "mtn_money"

PAWAPAY = {
    "BASE_URL": "https://fake.pawapay.test",
    "BEARER_TOKEN": "fake-token",
}

MTN_MOMO = {
    "BASE_URL": "https://fake.mtn.test",
    "API_USER_ID": "fake-user-id",
    "API_KEY": "fake-api-key",
    "SUBSCRIPTION_KEY": "fake-sub-key",
    "TARGET_ENVIRONMENT": "sandbox",
    "CALLBACK_URL": "",
}

MTN_DISBURSEMENT = {
    "BASE_URL": "https://fake.mtn.test",
    "API_USER_ID": "fake-user-id",
    "API_KEY": "fake-api-key",
    "SUBSCRIPTION_KEY": "fake-sub-key",
    "TARGET_ENVIRONMENT": "sandbox",
    "CALLBACK_URL": "",
    "CHECK_BALANCE_BEFORE_TRANSFER": False,
}

FLUTTERWAVE_PAYMENT = {
    "SECRET_KEY": "fake-flutterwave-key",
}

DEBUG = True

SECRET_KEY = "dev-only-insecure-secret-key-do-not-use-in-production"