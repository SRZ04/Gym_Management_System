from django.shortcuts import render
from django.http import HttpResponse


def gym_client(request):
    print("Gym Client View function executed.")
    return HttpResponse("Client Page")
