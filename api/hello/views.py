from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    params = {
        'title': 'Hello Django',
        'msg': 'This is a sample message.'
    }
    return render(request, 'hello/index.html', params)