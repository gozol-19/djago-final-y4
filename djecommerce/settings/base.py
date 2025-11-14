
# import os
# from decouple import config

# BASE_DIR = os.path.dirname(os.path.dirname(
#     os.path.dirname(os.path.abspath(__file__))))

# SECRET_KEY = config('SECRET_KEY')

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',

#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'allauth.socialaccount',
#     'crispy_forms',
#     'django_countries',
#     'allauth.socialaccount.providers.google',

#     'crispy_bootstrap4',  
#     'core'
# ]

# MIDDLEWARE = [
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'allauth.account.middleware.AccountMiddleware',
# ]

# ROOT_URLCONF = 'djecommerce.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'djecommerce.wsgi.application'

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_L10N = True
# USE_TZ = True

# # Static files (CSS, JavaScript, Images)
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# # Email Configuration (FOR DEVELOPMENT - uses console)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'



# # Email Configuration (uses Gmail via environment variables)

# # EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# # EMAIL_HOST = 'smtp.gmail.com'
# # EMAIL_PORT = 587
# # EMAIL_USE_TLS = True
# # EMAIL_HOST_USER = config('EMAIL_HOST_USER')
# # EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
# # DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# # Updated Django Allauth Settings (Fixed deprecated warnings)
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
# ACCOUNT_LOGIN_METHODS = {'username', 'email'}
# ACCOUNT_SIGNUP_FIELDS = ['email*', 'username*', 'password1*', 'password2*']
# ACCOUNT_RATE_LIMITS = {
#     'confirm_email': '1/3m',
# }
# ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 3
# ACCOUNT_EMAIL_CONFIRMATION_HMAC = True

# # Login/Logout settings
# ACCOUNT_LOGOUT_REDIRECT_URL = '/'
# LOGIN_REDIRECT_URL = '/'

# # Custom adapter to redirect after email confirmation
# ACCOUNT_ADAPTER = 'core.adapters.CustomAccountAdapter'

# # Default primary key type
# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Auth
# AUTHENTICATION_BACKENDS = (
#     'django.contrib.auth.backends.ModelBackend',
#     'allauth.account.auth_backends.AuthenticationBackend'
# )
# SITE_ID = 1

# # CRISPY FORMS
# CRISPY_TEMPLATE_PACK = 'bootstrap4'
# CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

# # Stripe Configuration (using decouple config only)
# USE_STRIPE_LIVE = config('USE_STRIPE_LIVE', default=False, cast=bool)
# if USE_STRIPE_LIVE:
#     STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
#     STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
# else:
#     STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
#     STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
 
 
    
# ACCOUNT_ADAPTER = 'core.adapters.CustomAccountAdapter'
  
  
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

SECRET_KEY = config('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'crispy_forms',
    'django_countries',
    'allauth.socialaccount.providers.google',

    'crispy_bootstrap4',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'djecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'djecommerce.wsgi.application'

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Phnom_Penh'
USE_I18N = True
USE_TZ = True

# Static and Media Files
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_in_env')]
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')

# Email Configuration (for development)
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# DEFAULT_FROM_EMAIL = 'webmaster@localhost'

# Optional: use Gmail for real emails
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Django Allauth Settings
ACCOUNT_AUTHENTICATION_METHOD = 'email'  # Use email to login
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SESSION_REMEMBER = True

# Redirects
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
LOGIN_REDIRECT_URL = '/'

# Custom adapter (if you use it)
ACCOUNT_ADAPTER = 'core.adapters.CustomAccountAdapter'

# Authentication
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)
SITE_ID = 1

# Crispy Forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap4'

# Stripe Configuration
USE_STRIPE_LIVE = config('USE_STRIPE_LIVE', default=False, cast=bool)
if USE_STRIPE_LIVE:
    STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY')
    STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY')
else:
    STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY')
    STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY')
