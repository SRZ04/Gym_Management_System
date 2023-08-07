from django.urls import path
from . import views

urlpatterns=[
    path('',views.gym_client,name='gym_client'),
]