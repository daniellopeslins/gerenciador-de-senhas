def exibir_menu():
    print("\n=== Gerenciador de Senhas ===")
    print("1. Adicionar nova senha")
    print("2. Visualizar senha existente")
    print("3. Atualizar senha existente")
    print("4. Excluir senha")
    print("5. Listar todos os serviços")
    print("6. Sair")
    print("========================")

def adicionar_senha(senhas):
    servico = input("Digite o nome do serviço (ex.: Gmail, Facebook): ").lower()
    if servico in senhas:
        print(f"O serviço '{servico}' já possui uma senha cadastrada!")
        return
    senha = input(f"Digite a senha para o serviço '{servico}': ")
    senhas[servico] = senha
    print(f"Senha para '{servico}' adicionada com sucesso!")

def visualizar_senha(senhas):
    servico = input("Digite o nome do serviço para visualizar a senha: ").lower()
    if servico in senhas:
        print(f"A senha para '{servico}' é: {senhas[servico]}")
    else:
        print(f"Não há senha cadastrada para o serviço '{servico}'.")

def atualizar_senha(senhas):
    servico = input("Digite o nome do serviço para atualizar a senha: ").lower()
    if servico in senhas:
        nova_senha = input(f"Digite a nova senha para '{servico}': ")
        senhas[servico] = nova_senha
        print(f"Senha para '{servico}' atualizada com sucesso!")
    else:
        print(f"Não há senha cadastrada para o serviço '{servico}'.")

def excluir_senha(senhas):
    servico = input("Digite o nome do serviço para excluir a senha: ").lower()
    if servico in senhas:
        del senhas[servico]
        print(f"Senha para '{servico}' excluída com sucesso!")
    else:
        print(f"Não há senha cadastrada para o serviço '{servico}'.")

def listar_servicos(senhas):
    if senhas:
        print("\nServiços cadastrados:")
        for servico in senhas:
            print(f"- {servico}")
    else:
        print("Nenhum serviço cadastrado ainda.")

def main():
    
    senhas = {}
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-6): ")
        
        if opcao == "1":
            adicionar_senha(senhas)
        elif opcao == "2":
            visualizar_senha(senhas)
        elif opcao == "3":
            atualizar_senha(senhas)
        elif opcao == "4":
            excluir_senha(senhas)
        elif opcao == "5":
            listar_servicos(senhas)
        elif opcao == "6":
            print("Saindo do gerenciador de senhas. Até mais!")
            break
        else:
            print("Opção inválida! Por favor, escolha um número entre 1 e 6.")
        
        
        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()
