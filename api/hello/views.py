from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title': 'Hello Django',
        'msg': 'This is a sample message.',
        'goto': 'next',
    }
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'Hello Next',
        'msg': 'This is next page.',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)