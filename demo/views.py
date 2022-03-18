from django.http import HttpResponse
from django.shortcuts import render

def first(request):
        return HttpResponse('First message from views')