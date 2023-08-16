from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html',{
        "name": 'Mauiricio Rosa'
    })

def contato(request):
    return render(request, 'temp.html')

def sobre(request):
    return HttpResponse('sobre')
