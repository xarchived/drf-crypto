from django.conf import settings

if not hasattr(settings, "CRYPTO"):
    settings.CRYPTO = dict()

DEBUG = settings.DEBUG
AMOUNT_MAX_DIGITS = settings.CRYPTO.get("AMOUNT_MAX_DIGITS", 30)
AMOUNT_DECIMAL_PLACES = settings.CRYPTO.get("AMOUNT_DECIMAL_PLACES", 0)
