## Estrutura de Rotas
As rotas utilizadas no sistema seguem o padrão Rest, onde requisições GET são referente a busca e POST referentes à atualização e criação.

## Dependência
* Comunicação com o banco de dados
Como se trata de uma aplicação usando a linguagem Python para acessar o banco de dados é feito o uso da ORM peewee, na qual é necessaria fazer a instalação e pode ser feita da seguinte maneira:
```bash
pip3 install peewee
```
```bash
pip3 install -U flask-cors
```
## Utilização Local

### Linux
* iniciar o serviço flask (necessario estar na pasta do repositorio)
 ```bash
source back_env/bin/activate
export FLASK_APP=appet_back.py
export FLASK_ENV=development
flask run
```


### Windows
* iniciar o serviço flask (necessario estar na pasta do repositorio)
```bash
windows_env\Scripts\activate.bat
set FLASK_APP=appet_back.py
set FLASK_ENV=development
flask run
```


## Rotas
### /ServiceSchedule
Rota para requisições referentes ao Horário Serviço.
#### POST
parâmetros aceitos:
* periodoId : ID referente ao período de tempo que o horário estará disponível.
* beginTime: Inicio do horário no qual o serviço estará disponível, o parâmetro deve ser passado no formado HHMMSS.
* endTime: Fim do horário no qual o serviço estará disponível, o parâmetro deve ser passado no formado HHMMSS.
* weekDay: Inteiro representando o dia da semana referente, 1 equivale domingo, 2 equivale segunda e assim por diante.
* schedule_id: ID referente ao Horário Serviço que irá receber a atualização de dados. Caso não seja informado este parâmetro é feita a criação de um novo objeto.
#### GET
Parâmetros aceitos:
* periodoId : ID referente ao período de tempo do horário para a busca.
* beginTime: Inicio do horário no qual será feita a busca, o parâmetro deve ser passado no formado HHMMSS.
* endTime: Fim do horário  no qual será feita a busca, o parâmetro deve ser passado no formado HHMMSS.
* weekDay: Inteiro representando o dia da semana referente, 1 equivale domingo, 2 equivale segunda e assim por diante.

### /AtivityTime
Rota para requisições referentes ao Período Atividade.
#### POST
Parâmetros aceitos:
* beginDate: Data inicio do período na qual estará ativo, o parâmetro deve ser passado no formado YYYYmmDD.
* endDate: Data fim do período na qual estará ativo, o parâmetro deve ser passado no formado YYYYmmDD.
* ownerId: ID referente ao usuário que estará operando nesse período.
* periodoAtvidadeId: ID referente ao Período Atividade que irá receber a atualização de dados. Caso não seja informado este parâmetro é feita a criação de um novo objeto.
#### GET
parâmetros aceitos:
* beginDate: Data inicio do período na qual a busca deve ser feita, o parâmetro deve ser passado no formado YYYYmmDD.
* endDate: Data fim do período na qual a busca deve ser feita, o parâmetro deve ser passado no formado YYYYmmDD.
* ownerId: ID referente ao usuário que é o dono do período buscado.
* periodoAtvidadeId: ID referente ao Período Atividade que deve ser buscado
### /Service
Rota para requisições referentes ao Serviço.
#### POST
Parâmetros aceitos:
* title: Titulo que será exibido no trabalho ofertado.
* about: Descrição que será exibida no trabalho ofertado.
* price: Float representando o valor do serviço ofertado.
* ownerId: ID referente ao usuário que será o ofertador do trabalho.
* typeService: ID do tipo de serviço no qual o serviço irá se enquadrar.
* hourService: array de inteiro contendo os ID de Horário Serviço no qual o serviço estará disponível.
* service_id: ID do serviço que irá ser atualizado com as novas informações passadas.
#### GET
parâmetros aceitos:
* title: Titulo que será exibido no trabalho ofertado.
* about: Descrição que será exibida no trabalho ofertado.
* price: Float representando o valor do serviço ofertado.
* ownerId: ID referente ao usuário que será o ofertador do trabalho.
* typeService: ID do tipo de serviço no qual o serviço irá se enquadrar.
* hourService: array de inteiro contendo os ID de Horário Serviço no qual o serviço estará disponível.

### /user
Rota para requisições referentes ao Usuário.
#### POST
Parâmetros aceitos:
* nomeUser: Nome do usuário no sistema.
* emailUser: Email do usuário no sistema.
* senha: Senha de acesso ao sistema.
* sobre: Descrição referente ao usuário.
* userId: ID do usuário para irá receber a atualização de dados, caso não seja informado é criado um novo usuário.
#### GET
parâmetros aceitos:
* nomeUser: Nome do usuário no sistema.
* emailUser: Email do usuário no sistema.
* senha: Senha de acesso ao sistema.
* sobre: Descrição referente ao usuário.
