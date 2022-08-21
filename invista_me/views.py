from django.shortcuts import render
from django.shortcuts import HttpResponse

# Create your views here.

def pagina_inicial(request):
    return HttpResponse('Pronto para investir!')

def pagina_contato(request):
    return HttpResponse('Informações de contato: \n juancostask@gmail.com')   

def minha_historia(request):
    pessoa = {
        'nome':'jonas',
        'idade':28,
        'hobby':'Games'
    }
    return render(request, 'investimentos/minha_historia.html',pessoa)

def novo_investimento(request):

    return render(request,'investimentos/novo_investimento.html')

def investimento_registrado(request):
    investimento ={
        'tipo_investimento': request.POST.get('TipoInvestimento')
    }
    return render(request,'investimentos/investimento_registrado.html',investimento)