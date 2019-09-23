# APPET

### Membros
[André Felipe](https://github.com/objetovazio)<br>
[Elimar Macena](https://github.com/elimarmacena)<br>
[Jackson Willian](https://github.com/jacksonwillian)<br>
[Jennifer Gonçalves](https://github.com/jennicg)<br>
[Lavínia Corteletti](https://github.com/lvnc)<br>
[Vinicius Freitas](https://github.com/Viniciusfr123)<br>

### Tecnologias
A aplicação faz uso das seguintes tecnologias:
* Flask - Framework Python utlizado no back-end.
* Peewee - ORM Python.
* ElephantSQL - Servidor em nuvem PostgreSQL.
* Angular 7 - Framework JavaScript utilizado no front-end.

### Descrição
Tendo em mente a crescente do mercado voltado para pet,  o sistema tem como objetivo facilitar o acesso de serviços relacionado à esse nicho, tanto do lado prestador de serviço quanto do contratante. Para facilitar a busca dos donos de animais por serviços voltados para pets, seria interessante ter um sistema que dispõe e organiza informações sobre empresas ou pessoas prestadoras desse tipo de serviço.

O prestador ao se cadastrar no sistema além de informar o serviço que irá fornecer, quanto também uma agenda informando a disponibilidade do serviço. As informações sobre o quadro de horários do profissional são de extrema relevância, pois sabendo qual dia da semana e intervalo de horário estará livre ou ocupado, é possível que haja um melhor planejamento, tanto do prestador de serviço, quanto do contratante.

O feedback do cliente também deve ter seu espaço, portanto, deseja-se poder avaliar com uma nota (de 1 a 5) e comentários, os serviços contratados após a conclusão de sua prestação. Futuramente, para recompensar bons profissionais e exibir suas qualidades para os potenciais clientes seria bem-vindo premiações como medalhas virtuais por número de trabalhos atendidos, anos de experiência no sistema, bom atendimento, entre outras.

### Diário de bordo
Disponivel no [link](https://docs.google.com/document/d/1MVYH5-1b3fXK6fe7tgVpnsW3LuPh4UKSqFxMpGxPlkY/edit?usp=sharing).

### PMC
Disponivel no [link](https://docs.google.com/spreadsheets/d/1KR7TdsCXbvCLtQgdvFrAiOKe6TqR2X25asrLdR7QSQ8/edit?usp=sharing).

### Requisitos do Sistema

#### Requisito Funcional

| ID:RF 01        |  Tipo Requisito: Requisito Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve ser capaz de controlar os horarios disponiveis de um prestador de serviços. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RF 02        |  Tipo Requisito: Requisito Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve ser capaz de exibir feedbacks que um prestador recebeu através de seus serivços. |
| Dependência     | RN 01      |
| Conflito      | -      |

| ID:RF 03        |  Tipo Requisito: Requisito Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve ser capaz de filtrar os serviços nele cadastrados. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RF 04        |  Tipo Requisito: Requisito Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve possibilitar pelo menos um meio de pagamento ao usuário. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RF 05        |  Tipo Requisito: Requisito Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve basear seus resultados de busca com base na localização do usuário. |
| Dependência     | -      |
| Conflito      | -      |

#### Requisito Não Funcional

| ID:RNF 01        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | Os serviços disponibilizados no sistema devem ser cadastrados pelos prórprios usuarios. |
| Dependência     | RNF02      |
| Conflito      | -      |

| ID:RNF 02        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | Para cadastrar um serviço no sistema é necessario que o prestador informe : dia da semana referente a disponibilidade, o intervalo de tempo que a prestação de serviço dura, o valor referente a este período somado a periodicidade que o profissional está disposto a ceder no dia em questão.. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RNF 03        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | Ao se cadastrar no sistema, o usuario deve informar os seguintes dados: nome, e-mail, endereço e telefone. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RNF 04        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | O usuario que deseja cadastrar um serviço no sistema deve informar os meios de pagamentos que serão aceitos para a contratação do serviço prestado. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RNF 05        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve rodar na plataforma Web, sendo possível acessá-lo através dos principais navegadores disponíveis no mercado. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RNF 06        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve ser responsivo. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RNF 07        |  Tipo Requisito: Requisito Não Funcional |
| ------------- |:-------------:|
| Descrição      | O sistema deve realizar o tratamento de dados, evitando possíveis falhas. |
| Dependência     | -      |
| Conflito      | -      |

#### Regras de Negócio

| ID:RN 01        |  Tipo Requisito: Regra de Negocio |
| ------------- |:-------------:|
| Descrição      | O cadastro de feedback só sera realizado pelo usuario após o prestador contratado realizar o serviço em questão. |
| Dependência     | -      |
| Conflito      | -      |

| ID:RN 02        |  Tipo Requisito: Regra de Negocio |
| ------------- |:-------------:|
| Descrição      | Só é possivel a contratação e prestação de serviço por usuarios cadastrados no sistema. |
| Dependência     | -      |
| Conflito      | -      |

### Modelagem do Sistema
#### Diagrama de Classes
<p align="center">
  <img src="https://github.com/objetovazio/Appet/blob/master/Documenta%C3%A7%C3%A3o/Diagramas/diag_classe.svg">
</p><br>

#### Protótipo de telas
[Protótipo estático](https://github.com/objetovazio/Appet/blob/master/Documenta%C3%A7%C3%A3o/Appet.pdf)<br>
[Protótipo navegável](https://www.figma.com/proto/iOUFdv7tBXAr7cgyb22xPp/Appet?node-id=1%3A2&scaling=contain)


### Modelo de Negócio
<p align="center">
  <img src="https://github.com/objetovazio/Appet/blob/master/Documenta%C3%A7%C3%A3o/Diagramas/Cópia de BMC - Template.png">
</p><br>

### Proposta de valor

<p align="center">
  <img src="https://github.com/objetovazio/Appet/blob/master/Documenta%C3%A7%C3%A3o/Diagramas/proposta de valor.png">
</p><br>
