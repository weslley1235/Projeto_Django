from django.shortcuts import render
from core.models import Products, Blog
from django.shortcuts import render, get_object_or_404

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

def produto(request):
    product = Products.objects.all() # Products.objects.all() -> Usado para recuperar todos os objetos de um modelo (Dados de uma tabela).

    data = {
        'product': product,
    }
    return render(request, 'produto.html', data)

def contato (request):
    return render(request, 'contato.html')

def blog(request):
    blog = Blog.objects.all()
    
    data = {
        'blog': blog,
        'title': 'Blog Django'
    }
    return render(request, 'blog.html', data)

#pagina single do blog com slug,url amigavel
def blog_single(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, 'blog_single.html', {'blog': blog})

def produto_single(request, id):
    product = get_object_or_404(Products, id=id) # get_object_or_404(Products, id=id) -> Usado para recuperar um único objeto com base em um critério específico, como um ID único.
    return render(request, 'produto_single.html', {'product': product})

