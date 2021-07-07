from django.apps import AppConfig


class ProductsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField' # customize the pk of Products model by using
# bigautofilter which is 64 bit integer.
    name = 'products'
