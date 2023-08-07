from django.urls import path
from . import views

urlpatterns=[
    path('',views.gym_admin,name='gym_admin'),
]