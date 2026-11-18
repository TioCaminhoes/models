# Respostas da atividade – Mini biblioteca

# 1. a. Não, O ModelForm é montando de acordo com o Model. Assim que é chamado os is_valid() no form, ele roda a validação do Model.

# b. clean campo pode ser utilizado para alterar algum valor ou analisar algum dado, e o validator para validar quem pode ou não pode entrar. Se o dado precisar remover os espaços, por exemplo, usa-se o clean campo. Se o dado precisar validar se está correto ou não, usa-se o validator

# c. como será feito uma analise de comparação, o clean() pode ser aplicado pois consegue analisar todos os dados. Como será feito uma alteração, o clean_title() pode ser aplicado, pois precisa alterar para remoção de espaços. Nessa ocasião é uma regra, então podemos utilizar o validator MaxValue para validar o máximo de paginas. Como aqui acontece uma comparação, o clean() pode ser utilizado: se não está disponível e o ISBN estiver vazio, adiciona um erro.

# 2. a. O livro é salvo com capa vazia em ambas ocasiões. O formulário não dá aviso nos dois casos, porque a capa é blank=True e o form acha que simplesmente não mandaram nada.

# b. Static são arquivos do sistema, e Media são arquivos enviados pelos usuários. Na mini biblioteca, static pode ser utilizado na logo ou alguma imagem que não irá sofrer alterações frequentemente. Já a Media, pode ser utilizado nas capas enviadas pelos usuários, podendo sofrer alterações a qualquer momento. 

# c. O banco guarda só o caminho da imagem, assim que a imagem é trocada, o Django muda a rota e altera no banco de dados. Portanto, a longo prazo, cria arquivos desnecessários, o que aumentaria o armazenamento. 

# d. A extensão é só parte do nome do arquivo e qualquer pessoa pode mudar. Nos meus testes, o falso.png (um texto renomeado) só foi barrado porque o ImageField usa o Pillow para abrir o arquivo e ver se é imagem de verdade. Outros cuidados: limitar o tamanho, para ninguém lotar o disco ou travar o servidor; limitar os tipos aceitos com validators;

# 3. a. Quem faz é a classe, herdada da view genérica. Se é valido: Chama form_valid(form), que faz o form.save() e redireciona para o get_sucess_url(). Se é invalido: chama form_invalid(form), que renderiza o template de novo, com form preenchido e as mensagens de erro

# b. A CreateView já monta os argumentos do form sozinha. No método que prepara o form , quando a requisição é POST ela já passa data=request.POST e files=request.FILES.

# c. O GET só pode mostrar coisas, nunca alterar dados. Por isso o GET mostra “Tem certeza?” e só o POST exclui. Para fazer a exclusão pelo metodo GET, basta abrir um link para apagar o livro, porém um clique não-intencional poderia acabar excluindo sem uma confirmação.

# d. Vantagem: menos código repetido. Listar, detalhar, criar, editar e excluir já vêm prontos, e a gente só configura atributos (model, template_name...) ou sobrescreve um método. o fluxo fica escondido na herança. Para entender o que é chamado e em que ordem, é preciso conhecer as classes-base. Quando usar função: em uma view simples ou muito diferente do padrão, que não é um CRUD, como uma página com lógica própria passo a passo (juntar vários forms, chamar uma API, gerar um relatório). Nesses casos uma função curta e direta fica mais clara do que sobrescrever vários métodos.

