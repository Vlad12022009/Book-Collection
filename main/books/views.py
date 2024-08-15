from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("<h1>Hello this is a book collection app</h1>")