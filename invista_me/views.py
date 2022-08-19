from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def pagina_contato(request):
    return HttpResponse('Informações de contato: \n juancostask@gmail.com')   

def minha_historia(request):
    return render(request, 'investimentos/minha_historia.html')