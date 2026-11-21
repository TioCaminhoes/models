# Sites Auxiliadores: https://docs.djangoproject.com/en/6.1/ref/databases/#postgresql-notes
#                     https://pypi.org/project/python-decouple/
#                     https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/


## 1. O SQLlite, como o próprio nome possui "lite", é uma versão básica de banco de dados, com diversas limitações. Em comparação com PostgresSQL, é uma versão "profissional", onde receber várias requisições ao mesmo tempo. Podemos utilizar o SQLlite para protótipos pequenos e acadêmicos e, quando for colocar em prática, migrar para PostgresSQL

## 2. De acordo com o site DjangoProject, O Django precisa de um adaptador que fale com o PostgreSQL. A documentação diz que o Django suporta PostgreSQL 15 ou superior e exige psycopg 3.1.12+ ou psycopg2 2.9.9+, sendo o psycopg 3 o recomendado. O suporte ao psycopg2 deve ser descontinuado no futuro. Instalação: python -m pip install "psycopg[binary]"

## 3. ENGINE: o backend do Django usado para falar com o banco. Para o PostgreSQL, django.db.backends.postgresql. NAME: o nome do banco (por exemplo, biblioteca_db). No SQLite, seria o caminho do arquivo. USER: o usuário do PostgreSQL com que a aplicação se conecta (por exemplo, biblioteca_user). PASSWORD: a senha desse usuário. HOST: o endereço do servidor (por exemplo, localhost). PORT: a porta do servidor. A padrão do PostgreSQL é 5432.

## 4. CREATE USER biblioteca_user WITH PASSWORD 'senha'; CREATE DATABASE biblioteca_db OWNER biblioteca_user ENCODING 'UTF8';

## 5. De acordo com o site DjangoProject, variáveis de ambiente são valores como DB_NAME=nome da biblioteca, guardados fora do código, no sistema operacional ou em um arquivo como o .env, e lidos pelo programa quando ele inicia. Senhas não se escrevem no código porque o Git guarda todo o histórico, então uma senha commitada continua acessível mesmo depois de apagada, e quem tiver acesso ao repositório passa a ter acesso ao banco.

## 6. python -m pip install python-decouple (está no arquivo "requirements.txt").
## from decouple import Csv, config
## SECRET_KEY = config('SECRET_KEY')
## DEBUG = config('DEBUG', default=False, cast=bool)
## ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())
## DATABASES = {'default': {
##     'ENGINE': 'django.db.backends.postgresql',
##     'NAME': config('DB_NAME'),
##     'USER': config('DB_USER'),
##     'PASSWORD': config('DB_PASSWORD'),
##     'HOST': config('DB_HOST'),
##     'PORT': config('DB_PORT'),
## }}

## 7. O .gitignore protege o .env e o db.sqlite3. O .env.example é o modelo do .env, com os nomes das variáveis e valores fictícios. Quem clonar o projeto, copia o arquivo para .env e preenche com os valores reais. Assim, ele documenta quais variáveis a aplicação exige, sem dizer nenhum segredo.

## 8. De acordo com o DjangoProject, SECRET_KEY: deve ser um valor grande e aleatório, mantido em segredo. Ela assina sessões e tokens, então se vazar, as assinaturas podem ser forjadas. DEBUG: em produção deve ficar desligado, porque vaza trechos do código, variáveis locais, configurações e bibliotecas usadas. Por isso o padrão em config é False. ALLOWED_HOSTS: com DEBUG = False, o Django não funciona sem um valor adequado nesta configuração.