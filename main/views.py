from django.shortcuts import render, Httpresponse

def homepage(request):
    return render(request, "index.html")

# Create your views here.

def test(request):
    return render(request, "test.html")

def check(request):
    return Httpresponse("салам класс Httpresponse")
