from django.shortcuts import render, HttpResponse, redirect
from .models import Investimento
from .forms import InvestimentoForm

# Create your views here.

# def pagina_inicial(request):
#     return HttpResponse('Pronto para investir!')

def pagina_contato(request):
    return HttpResponse('Informações de contato: \n juancostask@gmail.com')   

def minha_historia(request):
    pessoa = {
        'nome':'jonas',
        'idade':28,
        'hobby':'Games'
    }
    return render(request, 'investimentos/minha_historia.html',pessoa)

# def novo_investimento(request):

#     return render(request,'investimentos/novo_investimento.html')

# def investimento_registrado(request):
#     investimento ={
#         'tipo_investimento': request.POST.get('TipoInvestimento')
#     }
#     return render(request,'investimentos/investimento_registrado.html',investimento)

def meus_investimentos(request):
    dados = {
        'dados':Investimento.objects.all()
    }
    return render(request,'investimentos/meus_investimentos.html',context=dados)

def detalhe(request, id_investimento):
    dados = {
        'dados': Investimento.objects.get(pk=id_investimento)
    }
    return render(request,'investimentos/detalhe.html',dados)

def criar(request):
    if request.method =='POST':
        investimento_form = InvestimentoForm(request.POST)
        if investimento_form.is_valid():
            investimento_form.save()
        return redirect('meus_investimentos')
    investimento_form = InvestimentoForm()
    formulario = {
        'formulario': investimento_form
    }
    return render(request, 'investimentos/novo_investimento.html',context=formulario)

def editar(request,id_investimento):
    investimento = Investimento.objects.get(pk=id_investimento)
    if request.method =='GET':
        formulario = InvestimentoForm(instance=investimento)
        return render(request,'investimentos/novo_investimento.html',{'formulario': formulario})
    else:
        if request.method =='POST':
            formulario = InvestimentoForm(request.POST, instance=investimento)
        if formulario.is_valid():
            formulario.save()
        return redirect('meus_investimentos')
