from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect


def gms_home(request):
    print("GMS View function executed.")
   
    return HttpResponse("GMS Home World")
   
