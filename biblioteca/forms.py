from datetime import date

from django import forms
from biblioteca.models import Author, Book


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['name', 'nationality']

        labels = {
            'name': 'Nome',
            'nationality': 'Nacionalidade',
        }

        error_messages = {
            'name': {
                'required': 'O campo Nome é obrigatório.',
            },
        }


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'ano_publicado', 'disponivel', 'categories']

        labels = {
            'title': 'Título',
            'author': 'Autor',
            'ano_publicado': 'Ano de Publicação',
            'disponivel': 'Disponível',
            'categories': 'Categorias',
        }

        widgets = {
            'categories': forms.CheckboxSelectMultiple(),
            'author': forms.SelectMultiple(),
        }

        error_messages = {
            'title': {
                'required': 'O campo Título é obrigatório.',
            },
            'author': {
                'required': 'O campo Autor é obrigatório.',
            },
            'ano_publicado': {
                'invalid': 'Digite um ano válido, usando apenas números. Exemplo: 1999.',
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categories'].required = False

    def clean_title(self):
        title = self.cleaned_data['title']
        title = ' '.join(title.split())

        if len(title) < 3:
            raise forms.ValidationError(
                'O título precisa ter pelo menos 3 caracteres. '
                'Escreva um título mais completo.'
            )

        return title

    def clean_ano_publicado(self):
        ano = self.cleaned_data['ano_publicado']
        ano_atual = date.today().year

        if ano > ano_atual:
            raise forms.ValidationError(
                f'O ano de publicação não pode ser maior que {ano_atual}. '
                'Corrija o ano e tente novamente.'
            )

        return ano