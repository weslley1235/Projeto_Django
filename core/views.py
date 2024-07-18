from django.shortcuts import render

from core.models import Products
# Create your views here.
def index (request):
    context = {
        'curses': 'Programação de Computadores',
        'languages': ['Python','Java','JavaScript','C#'],
        'news':[
            {
                'title':'Nova versão do Django lançada!',
                'subtitle': 'Confira as novidades da versão 3.0',
                'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita reiciendis magnam nam ipsum dolore numquam corporis? In, alias eligendi necessitatibus dolorem cumque odit facere impedit, nesciunt sed, repellat porro. Laudantium!'
            },
             {
                'title':'Python',
                'subtitle': 'Especialistas afirmam que python é a melhor linguagem de programação atual!',
                'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita reiciendis magnam nam ipsum dolore numquam corporis? In, alias eligendi necessitatibus dolorem cumque odit facere impedit, nesciunt sed, repellat porro. Laudantium!'
            },
             {
                'title':'JavaScript',
                'subtitle': 'Especialistas afirmam que JavaScript é a melhor linguagem para front-end',
                'text': 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Expedita reiciendis magnam nam ipsum dolore numquam corporis? In, alias eligendi necessitatibus dolorem cumque odit facere impedit, nesciunt sed, repellat porro. Laudantium!'
            },
        ]
    }
    
    return render(request, 'index.html', context)

def contato (request):
    return render(request, 'contato.html')

def mercado (request):
    return render(request,'mercado.html')

def produto (request):
    product = Products.objects.all()

    data = {
        'products': product,
    }
    return render(request, 'produto.html', data)