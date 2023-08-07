from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


def gym_admin(request):
    print("Gym Admin View function executed.")
    template=loader.get_template('gym_admin_index.html')
    return HttpResponse(template.render())
