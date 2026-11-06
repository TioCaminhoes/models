from django.shortcuts import get_object_or_404, redirect, render

from biblioteca.forms import AuthorForm
from biblioteca.models import Author, Book
from django.db.models import Count

def listar_livros(request):
    livros = Book.objects.all()
    return render(request, 'lista_livros.html', {
        'livros': livros,
    })


def author_detail(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    return render(request, 'author_detail.html', {
            'author': author, 
            'books': author.books.all()
        })

def cadastrar_autor(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            Author.objects.create(
                name=form.cleaned_data['name'],
                nationality=form.cleaned_data['nationality']
            )
            return redirect('author_detail', author_id=Author.objects.last().id)
    else:
        form = AuthorForm()
    return render(request, 'cadastrarautor.html', {'form': form})

def listar_autores(request):
    autores = Author.objects.annotate(num_books=Count('books'))
    return render(request, 'listagem_autores.html', {'autores': autores})