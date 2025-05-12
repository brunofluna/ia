import os
from funcoes import cadastrar_usuario, menu, usuarios

os.system('cls')
menu()

while True:
    
    
    opcao = int(input('selecione a ação desejada: '))

    match opcao:
        case 1:
            os.system('cls')
            nome = input('Qual o nome do usuario? ')
            cpf = input('Informe o CPF: ')
            
            print(cadastrar_usuario(nome, cpf))
            menu()
            
        case 2:
            os.system('cls')
            print(usuarios)
            menu()
        case 3:
            os.system('cls')
            usuario = input("Qual usuario deseja atualizar? ")
            usuario_atualizado = input('Qual o novo nome? ')
            index = usuario.index(usuario)
            usuario[index] = usuario_atualizado
            menu()

        case 4:
            usuario = input("Qual usuario deseja deletar? ")
            
            index = usuario.index(usuario)
            usuarios.pop(index)
            menu()
        case 5:
            break
        case _:
            print('Opção inválida!')
