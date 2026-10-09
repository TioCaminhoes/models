from django.shortcuts import get_object_or_404, render

from biblioteca.models import Author, Book

def listar_livros(request):
    livros = Book.objects.all()
    return render(request, 'lista_livros.html', {'livros': livros})


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(
        request,
        'author_detail.html',
        {'author': author, 'books': author.books.all()},
    )
