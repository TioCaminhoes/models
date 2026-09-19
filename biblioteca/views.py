from django.shortcuts import render
from biblioteca.models import Livro

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})
