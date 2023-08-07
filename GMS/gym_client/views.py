from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def gym_client(request):
    print("Gym Client View function executed.")
    template=loader.get_template('gym_client_index.html')
    return HttpResponse(template.render())
