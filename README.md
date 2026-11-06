# Biblioteca

O campo `Book.author` usa `on_delete=PROTECT`: um autor que ainda tem livros
associados não pode ser apagado, evitando deixar esses livros sem autoria.
Para remover o autor, primeiro é preciso excluir os livros relacionados ou
associá-los a outro autor.

# Sobre o csrf token

por medidas de segurança, o django barra o cadastro e retorna a página de erro 403 - de acesso proíbido. 
Pesquisando mais nas settings, é possível encontrar um middleware padrão chamado  'django.middleware.csrf.CsrfViewMiddleware', onde ele barra caso não seja gerado um código único secreto (No meio das ligações entre views e template, é passado pelo middleware). Sem esse token, o Django não consegue diferenciar se o envio partiu do seu formulário legítimo ou de um ataque do tipo CSRF.