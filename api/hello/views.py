from django.shortcuts import render
from .forms import HelloForm

# Create your views here.
def index(request):
    params = {
        'title': 'Hello Django',
        'message': 'your data:',
        'form': HelloForm(),
    }

    if (request.method == 'POST'):
        params['message'] = '名前: ' + request.POST['name'] + \
            '<br>メール: ' + request.POST['mail'] + \
            '<br>年齢: ' + request.POST['age']
        params['form'] = HelloForm(request.POST)
    return render(request, 'hello/index.html', params)

def next(request):
    params = {
        'title': 'Hello Next',
        'msg': 'This is next page.',
        'goto': 'index',
    }
    return render(request, 'hello/index.html', params)

def form(request):
    msg = request.POST['msg']
    params = {
        'title': 'Hello Form',
        'msg': 'Hello ' + msg + '!!',
    }
    return render(request, 'hello/index.html', params)