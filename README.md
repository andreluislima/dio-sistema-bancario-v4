# 💳 Sistema Bancário: SantANDRÉ - V3 e V4 - POO

- Desafio 1: Refatorar o sistema anterior, para aplicar os princípios da Programação Orientada a Objetos (POO), como herança, polimorfismo, interfaces e classes abstratas.
- Desafio 2: Tornar o projeto funcional.

## ✅ Requisitos do Projeto

- Aplicar **conceitos fundamentais de POO**, com base no diagrama UML fornecido.

### 🔷 Especificações técnicas (baseadas no diagrama UML)

- **Classe `Conta`**
  - Atributos: `saldo`, `numero`, `agencia`, `cliente`, `historico`
  - Métodos: `saldo()`, `nova_conta()`, `sacar()`, `depositar()`
  - Associação com `Cliente` (1:N) e com `Historico` (1:1)

- **Classe derivada `ContaCorrente`** (herda de `Conta`)
  - Atributos adicionais: `limite`, `limite_saques`

- **Classe `Cliente`**
  - Atributos: `endereco`, `contas`
  - Métodos: `realizar_transacao()`, `adicionar_conta()`
  - Associação com `Conta` (1:N)

- **Classe derivada `PessoaFisica`** (herda de `Cliente`)
  - Atributos adicionais: `cpf`, `nome`, `data_nascimento`

- **Classe `Historico`**
  - Atributos: `transacoes`
  - Método: `adicionar_transacao(transacao: Transacao)`

- **Interface `Transacao`**
  - Método: `registrar(conta: Conta)`
  - Implementada por:
    - `Deposito` (atributo: `valor`)
    - `Saque` (atributo: `valor`)


## 📦 Diagrama UML

A modelagem do sistema segue o diagrama UML abaixo:

![UML Banco](./image.png)

## 📞 Contato

**André Lima**  
📧 andreluislima@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/andreluislima89)  
💻 [GitHub](https://github.com/andreluislima)
