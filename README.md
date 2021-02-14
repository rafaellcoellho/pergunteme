<p align="center">
  <a href="https://pergunteme.herokuapp.com/" target="_blank" rel="noopener noreferrer">
    <img alt="Logo" src="./logo.png" width="200px">
  </a>
</p>

<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT Licence"></a>
</p>

Trabalho final da cadeira de banco de dados. Usando Django e Postgres.

## Configurações iniciais

### Criando ambiente virtual

Usando [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/):

```bash
$ mkvirtualenv --python=python3.8 pergunteme
```

### Instalando Dependencias

Usando [poetry](https://python-poetry.org/):

```bash
$ poetry install
```

### Subindo banco de dados de desenvolvimento

Usando [docker](https://www.docker.com/) baixamos a imagem da versão 13.2 do postgres:

```bash
$ docker pull postgres:13.2 
```

Criamos a pasta onde vai persistir os dados no nosso banco local:

```shell
$ mkdir ~/External/Docker/postgres-13.2 
```

Agora é só subir o container com o seguinte comando:

```bash
$ docker run -d \
    --name postgres-13.2 \
    -e POSTGRES_PASSWORD=postgres \
    -p 5432:5432 \
    -v $HOME/External/Docker/postgres-13.2:/var/lib/postgresql/data \
    postgres:13.2
```

Note que eu usei a pasta criada anteriormente na hora de criar o volume.
Usando [psql](https://www.postgresql.org/docs/13/app-psql.html) vamos nos conectar a instância do banco:

```shell
$ psql -h localhost -p 5432 -U postgres -W
```

Após digitar a senha `postgres` que definimos ao subir o container, vamos criar o banco de dados:

```sql
postgres=# CREATE DATABASE pergunteme
WITH
   OWNER =  postgres
   ENCODING = 'UTF8'
   TABLESPACE = pg_default;
```

Por ultimos rodamos as migrações disponíveis:

```bash
$ python manage.py migrate
```

### Rodando o projeto

```bash
$ python manage.py runserver
```
