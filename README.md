# Biblioteca

Cada livro pode ter um ou mais autores. As migrações `0003`, `0004` e `0005`
adicionam a relação muitos-para-muitos, copiam os vínculos antigos e removem o
campo `ForeignKey`, nessa ordem. O vínculo reverso continua com o nome
`Author.books`, preservando a consulta usada pela página de detalhes do autor.

## Reverter a migração

Ao voltar para o modelo com `ForeignKey`, perde-se qualquer vínculo adicional
além do primeiro autor (escolhido pelo menor ID): uma chave estrangeira só pode
representar um autor por livro. A reversão interrompe com erro se algum livro
não tiver autor, pois não existe um valor válido para restaurar na chave
estrangeira obrigatória.

## Livros sem autores

Se o único autor de um livro for apagado, a relação muitos-para-muitos é
removida, mas o livro permanece cadastrado sem autores. `blank=False` impede
salvar o formulário do admin sem selecionar um autor; isso não é uma restrição
do banco e não cobre alterações feitas diretamente pelo ORM. Para garantir a
regra em toda a aplicação, as operações de criação/edição devem validar a
presença de pelo menos um autor, e a exclusão de autores deve impedir remover o
último vínculo (ou exigir sua substituição). Uma garantia também contra
escritas externas exige uma regra equivalente no banco, por exemplo um trigger.