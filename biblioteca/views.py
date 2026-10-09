from django.shortcuts import get_object_or_404, render
from django.db.models import Count

from biblioteca.models import Author, Book

def listar_livros(request):
    livros = Book.objects.prefetch_related('authors', 'categories')
    total_livros = livros.count()
    livros_disponiveis = livros.filter(disponivel=True).count()
    return render(
        request,
        'lista_livros.html',
        {
            'livros': livros,
            'total_livros': total_livros,
            'livros_disponiveis': livros_disponiveis,
            'livros_emprestados': total_livros - livros_disponiveis,
            'total_autores': Author.objects.annotate(
                book_count=Count('books', distinct=True)
            )
            .filter(book_count__gt=0)
            .count(),
        },
    )


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(
        request,
        'author_detail.html',
        {
            'author': author,
            'books': author.books.prefetch_related('categories').all(),
        },
    )
