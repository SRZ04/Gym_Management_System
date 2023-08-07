from django.urls import path
from . import views

urlpatterns=[
    path('',views.gym_trainer,name='gym_trainer'),
]