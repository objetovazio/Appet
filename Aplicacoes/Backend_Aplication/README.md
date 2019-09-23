## Estrutura de Rotas
As rotas utilizadas no sistema seguem o padrão Rest, onde requisições GET são referente a busca e POST referentes à atualização e criação.

## Utilização Local

* iniciar o serviço flask (necessario estar na pasta do repositorio)
 ```bash
source back_env/bin/active
export FLASK_APP=appet_back.py
export FLASK_ENV=development
flask run
```