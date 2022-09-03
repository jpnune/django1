from django.urls import path
from .views import index, contato, produto, login, resposta


urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('produto/<int:pk>', produto, name='produto'),
    path('login/', login),
    path('resposta/', resposta, name='resposta'),
]
