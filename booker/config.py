class Config:
    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'django-insecure-j%ohyh7lcnv+(xf5=9f5htx=_izeipj)z_xl8s_pq!q71dz^57'
    # Routes
    LOGIN_REDIRECT_URL = 'home/'
    LOGOUT_REDIRECT_URL = 'login/'

    # emails
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = 'kevinowidi@yahoo.com'
    EMAIL_HOST_PASSWORD = 'omeraJamach'

    # DEFAULT_FROM_EMAIL = 'noreply<no_reply@domain.com>'
    # HTML_MESSAGE_TEMPLATE = "registration/email_verify.html"
    # VERIFICATION_SUCCESS_TEMPLATE = "registration/email_success.html"
    # VERIFICATION_FAILED_TEMPLATE = "registration/email_failed.html"

    # Database configuration
    DATABASE_NAME = 'dee'
    DATABASE_USER = 'whoami'
    DATABASE_PASS = '@letmein24/7'