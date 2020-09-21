from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse, HttpRequest


# Create your views here.

def reg(request: HttpRequest):
    return HttpResponse("test")
