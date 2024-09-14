Testes para a classe HorarioAtendimento
=======================================

Francisco P. Guimarães e Laura Pivoto Ambrosio Guimarães.

Descrição
---------

Este projeto contém uma suíte de testes unitários para a classe HorarioAtendimento, utilizando o framework unittest e a funcionalidade de mocks da biblioteca unittest.mock. A classe HorarioAtendimento faz parte de um sistema para gerenciar horários de atendimento de professores e a reserva de salas em uma instituição educacional.

### Estrutura

*   **Classe de Testes**: test\_horario\_atendimento
    
*   **Mocks**: Utiliza o MagicMock para simular o comportamento do serviço HorarioAtendimentoService, que é passado como dependência para a classe HorarioAtendimento.
    

Instalação
----------

Certifique-se de que você tenha o unittest configurado corretamente em seu ambiente. Nenhuma instalação adicional é necessária se estiver utilizando uma distribuição Python padrão.


Isso executará todos os testes presentes na pasta tests.

Cobertura de Testes
-------------------

Os testes cobrem tanto cenários positivos quanto negativos. Abaixo está uma descrição detalhada de cada teste, categorizada em diferentes funcionalidades testadas.

### Testes de Horários de Atendimento

#### Testes Positivos

1.  **test\_buscar\_horario\_chris**: Verifica se o horário do professor "Chris" é retornado corretamente.
    
2.  **test\_buscar\_predio\_atendimento\_laura**: Verifica se o prédio onde o professor "Laura" atende é retornado corretamente.
    
3.  **test\_buscar\_horario\_pedro**: Verifica se os dados do professor "Pedro" são retornados corretamente.
    
4.  **test\_buscar\_horario\_ana**: Verifica se o horário do professor "Ana" é retornado corretamente.
    

#### Testes Negativos

1.  **test\_buscar\_horario\_predio\_fora\_intervalo**: Verifica a busca por um prédio que não existe, esperando o retorno "Predio não existe".
    
2.  **test\_buscar\_horario\_professor\_inexistente**: Verifica o comportamento ao buscar um professor inexistente.
    

### Testes de Salas

#### Testes Positivos

1.  **test\_buscar\_sala**: Verifica a busca por uma sala específica e seus horários livres.
    
2.  **test\_buscar\_sala\_20**: Verifica a busca pela sala 20 e seus horários livres.
    

#### Testes Negativos

1.  **test\_buscar\_sala\_com\_numero\_inexistente**: Testa a busca por uma sala inexistente.
    
2.  **test\_buscar\_por\_sala\_predio\_fora\_do\_intervalo**: Verifica a busca por uma sala em um prédio inválido.
    

### Testes de Inserção de Horários

#### Testes Positivos

1.  **test\_inserir\_horario**: Testa a inserção de um novo horário de atendimento, validando o sucesso com o retorno True.
    
2.  **test\_inserir\_horario\_noturno**: Verifica a inserção de um horário noturno válido.
    

#### Testes Negativos

1.  **test\_inserir\_horario\_invalido**: Verifica a inserção de um horário com formato inválido.
    
2.  **test\_inserir\_horario\_periodo\_invalido**: Verifica a inserção de um horário com um período inválido, como "Madrugada".
    
3.  **test\_inserir\_horario\_sala\_invalida**: Testa a inserção de um horário em uma sala inválida.
    

### Testes de Reserva de Sala

#### Testes Positivos

1.  **test\_reservar\_sala**: Verifica se a reserva de uma sala é realizada com sucesso para um horário disponível.
    

#### Testes Negativos

1.  **test\_reservar\_sala\_inexistente**: Verifica o comportamento ao tentar reservar uma sala inexistente.
    
2.  **test\_reservar\_sala\_sem\_horarios**: Verifica o comportamento ao tentar reservar uma sala que não possui horários disponíveis.
    
3.  **test\_reservar\_sala\_horario\_indisponivel**: Verifica a reserva de uma sala em um horário que não está disponível.
    
4.  **test\_reservar\_sala\_falha\_ao\_reservar**: Verifica o comportamento quando a tentativa de reserva falha por outro motivo.
    

Dependências
------------

*   **unittest**: Para criar e executar os testes.
    
*   **unittest.mock**: Para simular o comportamento do serviço de horários.
    

Estrutura de Arquivos
---------------------

*   **tests/horariosTest.py**: Arquivo contendo todos os testes.
    
*   **tests/horariosMock.py**: Arquivo contendo os mocks dos horários e das salas.
    
*   **c214/horarios.py**: Implementação da classe HorarioAtendimento.
    

Conclusão
---------

Esta suíte de testes foi projetada para garantir a robustez e a confiabilidade das funcionalidades relacionadas a horários de atendimento e reserva de salas, cobrindo uma ampla gama de cenários positivos e negativos.
