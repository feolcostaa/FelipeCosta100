from django.shortcuts import render
from django.http import Http404

# receitas/views.py
def home(request):
    return render(request,'receitas/home.html')

def receita_detail(request, id):
    # Cria o dicionário de contexto com os dados da receita
    context = {
        'receita_id': id,
        'receita_title': f'Receita Detalhada ({id})',
        'receita_description': f'Esta é a descrição detalhada da receita com ID ({id})'
    }

    # Renderiza o template 'receita_detail.html' e passa o contexto para ele
    return render(request, 'receitas/receita_detail.html', context)