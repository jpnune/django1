from django.shortcuts import render, get_object_or_404
from .models import Produto, Cliente, Login
from django.http import HttpResponse
from django.template import loader

def resposta(request):
    dados = Login.objects.all()
    #pegar os dados direto do banco
    #for c in dados:
    #    print('nome =', c.email)

    context = {
        'dados': dados
    }
    return render(request, 'resposta.html', context)


def index(request):
    """renderiza a pagina index"""
    produtos = Produto.objects.all()
    #p = list(produtos)
    #clientes = Cliente.objects.all()

    context = {
        'curso': 'Programação web django Framework',
        'curso2': 'outro curso de programação',
        'produtos': produtos,
        #'clientes': clientes,
        #'p': p[0],
    }
    return render(request, 'index.html', context)


def contato(request):
    """renderiza a pagina de contato"""
    print('contato', request)
    return render(request, 'contato.html')


def produto(request, pk):
    #prod = Produto.objects.get(id=pk)

    prod = get_object_or_404(Produto, id = pk)
    context = {
        'produto': prod,
    }
    return render(request, 'produto.html', context)


def login(request):
    log = request.POST
    print(log)
    email = log['email']
    senha = log['senha']
    print(email, senha)
    cadastro = Login(email=email, senha=senha, )
    cadastro.save()
    return render(request, 'login.html')


def error404(request, ex):
    template = loader.get_template('404.html')
    return HttpResponse(content=template.render(),
                        content_type='text/html; charset=utf8',
                        status=404)


def error500(request):
    template = loader.get_template('500.html')
    return HttpResponse(content=template.render(),
                        content_type= 'text/html; charset=utf8',
                        status=500)



