# Sistema Bancário em Python

Um sistema bancário desenvolvido em **Python** para praticar conceitos fundamentais de programação, Programação Orientada a Objetos (POO), estruturas de dados e lógica de sistemas.

O projeto simula operações básicas de um sistema de contas bancárias diretamente pelo terminal.

## Sobre o projeto

O objetivo deste projeto é colocar em prática conceitos que estou aprendendo em Python, criando um sistema simples de gerenciamento de contas.

Atualmente, o sistema trabalha com contas bancárias e permite realizar operações como consulta de saldo e movimentação de dinheiro.

## Funcionalidades

* Criar contas bancárias
* Armazenar múltiplas contas
* Consultar contas cadastradas
* Consultar saldo
* Realizar depósitos
* Realizar saques
* Transferir dinheiro entre contas
* Validar saldo disponível
* Buscar contas pelo número

## Tecnologias

* **Python 3**
* Programação Orientada a Objetos (POO)
* Listas
* Loops
* Condicionais
* Funções
* Métodos
* Classes e objetos

## Estrutura do projeto

```text
system_accounts_banking/
├── main.py
└── README.md
```

## Exemplo

O sistema trabalha com contas que possuem informações como:

```text
Titular: Carlos
Número da conta: 123
Saldo: R$ 200.00
```

Uma transferência pode seguir o fluxo:

```text
Conta de origem
      ↓
Verificar saldo
      ↓
Retirar valor
      ↓
Conta de destino
      ↓
Depositar valor
```

## Como executar

Clone o repositório:

```bash
git clone https://github.com/SEU-USUARIO/system-accounts-banking.git
```

Entre na pasta:

```bash
cd system-accounts-banking
```

Execute:

```bash
python3 main.py
```

## Objetivo de aprendizado

Este projeto faz parte dos meus estudos de programação e tem como objetivo desenvolver minha capacidade de construir sistemas utilizando Python.

Durante o desenvolvimento, estou praticando principalmente:

* Classes e objetos
* `self`
* Métodos
* Listas de objetos
* Busca de objetos em listas
* `for`
* `if/else`
* Entrada de dados pelo terminal
* Manipulação de valores
* Validação de operações
* Organização de código

## Próximos passos

Algumas melhorias planejadas:

* [ ] Finalizar sistema de transferências
* [ ] Melhorar validações
* [ ] Criar menu interativo
* [ ] Impedir operações inválidas
* [ ] Adicionar histórico de transações
* [ ] Salvar contas em arquivo
* [ ] Criar persistência com banco de dados
* [ ] Melhorar organização do projeto

## Status

🚧 **Em desenvolvimento**

Este projeto está sendo desenvolvido como parte dos meus estudos de Python e POO.

## Autor

**William Roque**

Estudante de programação com foco em desenvolvimento de software e backend.

---

Este projeto é educacional e foi desenvolvido para fins de estudo.
