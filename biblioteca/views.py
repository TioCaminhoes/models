from django.db.models import Count
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from biblioteca.forms import AuthorForm, BookForm
from biblioteca.models import Author, Book


class LivroListView(ListView):
    model = Book
    template_name = 'lista_livros.html'
    context_object_name = 'livros'

    def get_queryset(self):
        return Book.objects.order_by('title')  

class LivroFormMixin:
    model = Book
    form_class = BookForm
    template_name = 'livroform.html'     
    titulo = ''
    botao = ''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = self.titulo
        context['botao'] = self.botao
        return context

    def get_success_url(self):
        return reverse('author_detail', kwargs={'author_id': self.object.author.first().id})

class LivroCreateView(LivroFormMixin, CreateView):
    titulo = 'Novo livro'
    botao = 'Cadastrar livro'

class LivroUpdateView(LivroFormMixin, UpdateView):
    pk_url_kwarg = 'book_id'            
    titulo = 'Editar livro'
    botao = 'Salvar alterações'

class LivroDeleteView(DeleteView):
    model = Book
    pk_url_kwarg = 'book_id'
    template_name = 'livro_confirm_delete.html'
    success_url = reverse_lazy('listar_livros')

class AuthorDetailView(DetailView):      
    model = Author
    template_name = 'author_detail.html'
    context_object_name = 'author'
    pk_url_kwarg = 'author_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = self.object.books.all()
        return context

class AuthorCreateView(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'cadastrarautor.html'

    def get_success_url(self):
        return reverse('author_detail', kwargs={'author_id': self.object.pk})

class AuthorListView(ListView):
    model = Author
    template_name = 'listagem_autores.html'
    context_object_name = 'autores'

    def get_queryset(self):
        return Author.objects.annotate(num_books=Count('books'))

class SobreView(TemplateView):
    template_name = 'sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = Book.objects.count()
        context['disponiveis'] = Book.objects.filter(disponivel=True).count()
        return context
