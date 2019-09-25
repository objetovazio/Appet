## Estrutura de Rotas
As rotas utilizadas no sistema seguem o padrão Rest, onde requisições GET são referente a busca e POST referentes à atualização e criação.

## Dependência
* Comunicação com o banco de dados
Como se trata de uma aplicação usando a linguagem Python para acessar o banco de dados é feito o uso da ORM peewee, na qual é necessaria fazer a instalação e pode ser feita da seguinte maneira:
```bash
pip3 install peewee
```

## Utilização Local

* iniciar o serviço flask (necessario estar na pasta do repositorio)
 ```bash
source back_env/bin/active
export FLASK_APP=appet_back.py
export FLASK_ENV=development
flask run
```