from django.shortcuts import render
import requests


def index(request):
    respones = requests.get('https://saurav.tech/NewsAPI/top-headlines/category/health/in.json')
    post=respones.json()
    data=post['articles']
    return render(request,"index.html",{"data":data})


