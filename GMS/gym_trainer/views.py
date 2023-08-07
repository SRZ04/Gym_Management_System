from django.shortcuts import render
from django.http import HttpResponse


def gym_trainer(request):
    print("Gym Trainer View function executed.")
    return HttpResponse("Trainer Page")
