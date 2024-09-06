from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("<h1>Welcome to my Fashion Blog</h1>")
def categories(request):
    return HttpResponse("<h1>Categories page</h1>")
def about(request):
    return HttpResponse("<h1>about page</h1>")
def shop(request):
    return HttpResponse("<h1>shop page</h1>")
def contact(request):
    return HttpResponse("<h1>contact us page</h1>")