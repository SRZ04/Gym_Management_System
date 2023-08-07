from django.apps import AppConfig


class AdminConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "gym_admin"
    verbose_name= 'Gym Admin'
