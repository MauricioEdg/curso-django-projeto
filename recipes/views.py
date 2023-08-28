from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html',context = {
        "name": 'Mauiricio Rosa'
    })

def contato(request):
    return render(request, 'recipes/contato.html',context= {
        "name": "Mauricio"
    })
