from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def main(request):
    return HttpResponse('<h1>HELLO WORLD</h1>')