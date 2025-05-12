class SistemaUsuarios:
    def __init__(self):
        self.usuarios = []

    def criar_usuario(self):
        print("\n=== Criar Novo Usuário ===")
        nome = input("Digite o nome: ")
        email = input("Digite o email: ")
        idade = input("Digite a idade: ")
        
        usuario = {
            "id": len(self.usuarios) + 1,
            "nome": nome,
            "email": email,
            "idade": idade
        }
        
        self.usuarios.append(usuario)
        print("Usuário criado com sucesso!")

    def listar_usuarios(self):
        print("\n=== Lista de Usuários ===")
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
            return
        
        for usuario in self.usuarios:
            print(f"\nID: {usuario['id']}")
            print(f"Nome: {usuario['nome']}")
            print(f"Email: {usuario['email']}")
            print(f"Idade: {usuario['idade']}")

    def buscar_usuario(self):
        print("\n=== Buscar Usuário ===")
        id_busca = int(input("Digite o ID do usuário: "))
        
        for usuario in self.usuarios:
            if usuario['id'] == id_busca:
                print(f"\nID: {usuario['id']}")
                print(f"Nome: {usuario['nome']}")
                print(f"Email: {usuario['email']}")
                print(f"Idade: {usuario['idade']}")
                return
        
        print("Usuário não encontrado!")

    def atualizar_usuario(self):
        print("\n=== Atualizar Usuário ===")
        id_atualizar = int(input("Digite o ID do usuário: "))
        
        for usuario in self.usuarios:
            if usuario['id'] == id_atualizar:
                usuario['nome'] = input("Digite o novo nome: ")
                usuario['email'] = input("Digite o novo email: ")
                usuario['idade'] = input("Digite a nova idade: ")
                print("Usuário atualizado com sucesso!")
                return
        
        print("Usuário não encontrado!")

    def remover_usuario(self):
        print("\n=== Remover Usuário ===")
        id_remover = int(input("Digite o ID do usuário: "))
        
        for i, usuario in enumerate(self.usuarios):
            if usuario['id'] == id_remover:
                del self.usuarios[i]
                print("Usuário removido com sucesso!")
                return
        
        print("Usuário não encontrado!")

def menu():
    print("\n=== Sistema de Gerenciamento de Usuários ===")
    print("1. Criar usuário")
    print("2. Listar usuários")
    print("3. Buscar usuário")
    print("4. Atualizar usuário")
    print("5. Remover usuário")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    sistema = SistemaUsuarios()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            sistema.criar_usuario()
        elif opcao == "2":
            sistema.listar_usuarios()
        elif opcao == "3":
            sistema.buscar_usuario()
        elif opcao == "4":
            sistema.atualizar_usuario()
        elif opcao == "5":
            sistema.remover_usuario()
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main() 