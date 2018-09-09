# Desafio(Código)

Este repositório é uma exemplificação de uma solução referente ao repositório [**Challenge**](https://github.com/phakiller/challenge).

### Explicação

Foi criada uma aplicação com *Flask*, onde a mesma tem três "sub aplicações". Cada Sub Aplicação tem suas próprias responsabilidades e peculiaridades, assim, cada uma representa um serviço. Cada Sub Aplicação foi nomeada de **Serviço A**, **Serviço B** e **Serviço C**.

O ***Serviço A***, interage com um Banco de Dados, PostgreSQL. Esse serviço é responsável por trazer informações de Clientes com suas respectivas dividas. Possui também uma rota de autenticação, onde é gerado um Token para ser possível consumir as outras rotas do ***Serviço A***.

O ***Serviço B***, interage com um Banco NoSQL, MongoDB. Esse serviço é responsável por trazer informações de Clientes com seus respectivos bens.

O ***Serviço C***, interage com um Banco NoSQL, Elasticsearch. Esse serviço é resposável por trazer informações de Clientes com suas respectivas movimentações financeiras.

Escolhi o *Flask*, pois trabalho com ele e consequentemente mais familiaridade.

A Aplicação e os Bancos foram *Dockerizados*. Os Bancos já tem alguns dados para teste.

### Tecnologias Utilizadas

* [**Python**](https://www.python.org)
    * [**Flask**](http://flask.pocoo.org)
    * [**Flask RESTFul**](https://flask-restful.readthedocs.io/en/latest/)
    * [**Flasgger**](https://github.com/rochacbruno/flasgger)
* [**PostgreSQL**](https://www.postgresql.org)
* [**MongoDB**](https://www.mongodb.com)
* [**Elasticsearch**](https://www.elastic.co/products/elasticsearch)
* [**Docker**](https://www.docker.com)

# Utilização

### Requisitos

* [**Docker**](https://www.docker.com)
* [**Docker Compose**](https://docs.docker.com/compose/install/)
* Dar permissões nas pastas, *mongodv_volume* e *elasticsearch_volume*. (chmod 777)

### Subindo o sistema

1. Clone ou faça o download deste repositório.

2. Dentro da pasta execute o comando para dar permissões nas pastas de volume:
    ```sh
    sudo chmod -R 777 ./mongodb_volume && chmod -R 777 ./elasticsearch_volume
    ```

3. Ainda dentro da pasta, execute o seguinte comando no terminal:
    ```sh
    docker-compose up --build --remove-orphans -d
    ```
4. Entre no link [**localhost:6606/challenge-api-docs**](http://localhost:6606/challenge-api-docs/).
Esse link dará o acesso ao Swagger onde você poderá fazer requisições para os EndPoints dos serviços.

5. Para parar os serviços, basta executar o seguinte comando no terminal, ainda dentro da pasta do projeto:
    ```sh
    docker-compose down
    ```

### Interagindo com o sistema

Todos os serviços tem rotas onde é necessário passar algum tipo de identificador na rota:
![Rotas com parametros](https://raw.githubusercontent.com/phakiller/code_challenge/master/images/parameters_routes.png "Rotas com parametros")

Você pode conseguir esses identificadores consumindo as outras rotas:

> - /service-a/v1/customer &rightarrow; /service-a/v1/customer/{tax_id}
> - /service-a/v1/debt &rightarrow; /service-a/v1/debt/{debt_id}
> - /service-b/v1/customer &rightarrow; /service-b/v1/customer/{tax_id}
> - /service-c/v1/customer &rightarrow; /service-c/v1/customer/{tax_id}

#### Serviço A

> Para interagir com as rotas do *Serviço A*, é necessário fazer o login na rota, */service-a/v1/login*.
> - Usuário: teste
> - Senha: senha123

##### Pegando o Token

1. Com o Swagger aberto, clique na rota de login:
![Tela Inicial - Swagger](https://raw.githubusercontent.com/phakiller/code_challenge/master/images/swagger_initial_login_route.png "Tela Inicial - Swagger")

2. Depois da rota aberta, clique em *Try it out*:
![Tela Rota de Login - Aberta](https://raw.githubusercontent.com/phakiller/code_challenge/master/images/swagger_token_service_a.png "Tela Rota de Login - Aberta")

3. Logo em seguida clique em, *Execute*:
    > Obs.: Não será necessário modificar o usuário e senha.

![Tela Rota de Login - Execute](https://raw.githubusercontent.com/phakiller/code_challenge/master/images/swagger_token_execute.png "Tela Rota de Login - Execute")

4. Role a página para baixo para pegar o token, ele estará no *Response Body*:
![Tela Rota de Login - Get Token](https://raw.githubusercontent.com/phakiller/code_challenge/master/images/swagger_get_token.png "Tela Rota de Login - Get Token")

> O Token tem validade de 1 hora.

Para consumir as outras rotas do *Serviço A* basta repetir os passos **1, 2, 3,** utilizando o token que foi gerado na rota de Login.
![Tela - Rota do Serviço A](https://raw.githubusercontent.com/phakiller/code_challenge/master/images/swagger_another_rote_service_a.png "Tela - Rota do Serviço A")

#### Serviço B e Serviço C

Os Serviços B e C tem a mesma mecânica, não tem a peculiaridade do Serviço A onde temos a rota de Login e precisamos do Token para interagir com as outras rotas.

Basta repetir os passos os mesmos passos do Serviço A, porém não é necessário o Token de autenticação.

#### Interação sem o Swagger

Para interagir com a aplicação direto, sem o Swagger utilize esta URL como base:
* http://localhost:6606

Os prefixos dos serviços são:
* **Serviço A** &rightarrow; /service-a/v1
    * /login ***[POST]***
    * /customer ***[GET]***
    * /customer/{tax_id} ***[GET]***
    * /debt ***[GET]***
    * /debt/{debt_id} ***[GET]***
* **Serviço B** &rightarrow; /service-b/v1
    * /customer ***[GET]***
    * /customer/{tax_id} ***[GET]***
* **Serviço C** &rightarrow; /service-c/v1
    * /customer ***[GET]***
    * /customer/{tax_id} ***[GET]***

# Notas

* As Bases de Dados já vem com alguns dados previamente inseridos.

* Os dados do PostgreSQL são inseridos toda vez que ele sobe, diferente do MongoDB e Elasticsearch que são mapeados para fora do *Container*.

* O arquivo com as variaveis de ambiente, *flask.env*, está no repositório para fins de teste. Nunca coloque dados sensiveis em repositórios, mesmo se sejam privados.

* Os dados inseridos nas bases de dados previamente, não condizem com a vida real.

* Se for necessário inserir mais dados:
    * PostgreSQL: Adicionar os dados no arquivo, *create_db_with_informations*, dentro da pasta *postgres_docker*.
    * MongoDB: Adicionar os dados pelo script, *insert_mongo_data.py*, que está na raiz do projeto.
    * Elasticsearch: Adicionar os dados pelo script, *insert_elasticsearch_data.py*, que está na raiz do projeto.

# Agradecimentos

* [**SWAPI - The Star Wars API**](https://swapi.co)