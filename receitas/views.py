# receitas/views.py
from django.shortcuts import render, get_object_or_404 
# Importe get_object_or_404
from .models import Receita # <--- Importe o seu modelo Receita
# Esta é a view que já existe para a página inicial
def home(request):
    # No futuro, você pode querer buscar as últimas receitas aqui para exibir na home
    return render(request, 'receitas/home.html')
# Nova view para exibir os detalhes de uma receita específica
def receita_detail(request, id): # 'id' é o parâmetro que vem da URL
    receita = get_object_or_404(Receita, pk=id) # 'pk' significa Chave Primária (Primary Key), que é o ID
    context = {
        'receita': receita, # Passamos o objeto 'receita' inteiro para o template
    }
    return render(request, 'receitas/receita_detail.html', context)


def pesquisar_receitas(request):
    """
    View para realizar a busca de receitas.
    """
    # Pega o valor do parâmetro 'q' da URL (?q=bolo)
    query = request.GET.get('q')

    # Se o parâmetro 'q' existir na URL, faz a busca
    if query:
        # Filtra as receitas cujo título contém o texto da busca (ignorando maiúsculas/minúsculas)
        # Atenção: 'titulo' deve ser o nome exato do campo no seu models.py
        resultados = Receita.objects.filter(title__icontains=query) 
    else:
        # Se não houver termo de busca, retorna uma lista vazia
        resultados = []

    # Cria o contexto para enviar os dados para o template
    context = {
        'query': query,
        'resultados': resultados,  # <-- Corrigido o ; para :
    }

    # Renderiza o template 'pesquisa.html' com os resultados
    return render(request, 'receitas/pesquisa.html', context)