# Biblioteca

O campo `Book.author` usa `on_delete=PROTECT`: um autor que ainda tem livros
associados não pode ser apagado, evitando deixar esses livros sem autoria.
Para remover o autor, primeiro é preciso excluir os livros relacionados ou
associá-los a outro autor.