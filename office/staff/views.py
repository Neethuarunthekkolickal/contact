from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render (request,"index.html")
def about(request):
    return render(request,"about.html")
def blog (request):
    return render (request,"blog.html")
def class1(request):
    return render (request,"class.html")
def hello(request):
    return render (request,"hello.html")
 