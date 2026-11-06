from django import forms
from biblioteca.models import Author

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
