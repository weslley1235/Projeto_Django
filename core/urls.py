
from django.urls import path
#foi feito o importe do include acima

#import das views index e contato criadas no core/views
from core.views import index,produto,contato,produto_single

urlpatterns = [
    path('', index, name='index'),
    path('produto', produto, name='produto'),
    path('contato', contato, name='contato'),
    path('produto/<int:id>/', produto_single, name='produto_single')
]

# acima o "path('', index)" indica que quando acessar a raiz do site será chamado a view index
# o "path('contato', contato)" indica que quando acessar a rota contato será chamado a view contato