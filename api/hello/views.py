from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request, id, nickname):
    result = 'your id:' + str(id) + ', nickname:' + nickname
    return HttpResponse(result)