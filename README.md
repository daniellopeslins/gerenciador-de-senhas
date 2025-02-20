# Gerenciador de Senhas em Python

Bem-vindo ao **Gerenciador de Senhas**, um aplicativo simples e interativo baseado em texto, desenvolvido em Python, que permite armazenar, visualizar, atualizar e excluir senhas de forma prática no terminal. Ideal para quem quer organizar suas credenciais de maneira básica ou aprender mais sobre funções, loops e estruturas de dados em Python!

Este projeto utiliza um dicionário em memória para gerenciar senhas associadas a serviços (como "Gmail" ou "Facebook"), oferecendo uma interface amigável com opções em um menu.

## Funcionalidades

- **Adicionar Senha**: Registre uma nova senha para um serviço.
- **Visualizar Senha**: Consulte a senha de um serviço existente.
- **Atualizar Senha**: Modifique a senha de um serviço já cadastrado.
- **Excluir Senha**: Remova um serviço e sua senha do gerenciador.
- **Listar Serviços**: Veja todos os serviços atualmente cadastrados.
- **Interface Interativa**: Menu simples no terminal com validação básica de entradas.

## Pré-requisitos

- **Python**: Versão 3.x instalada. Não são necessárias bibliotecas externas!

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/daniellopeslins/gerenciador-de-senhas.git
   cd gerenciador-de-senhas

2. Execute o programa:
   ```bash
   python gerenciador_senhas.py

3. Siga as instruções no terminal para interagir com o menu!
   ```bash
   === Gerenciador de Senhas ===
   1. Adicionar nova senha
   2. Visualizar senha existente
   3. Atualizar senha existente
   4. Excluir senha
   5. Listar todos os serviços
   6. Sair
   ========================
   Escolha uma opção (1-6): 1
   Digite o nome do serviço (ex.: Gmail, Facebook): gmail
   Digite a senha para o serviço 'gmail': minhaSenha123
   Senha para 'gmail' adicionada com sucesso!
   
   Pressione Enter para continuar...

=== Gerenciador de Senhas ===
Escolha uma opção (1-6): 2
Digite o nome do serviço para visualizar a senha: gmail
A senha para 'gmail' é: minhaSenha123

Pressione Enter para continuar...
