from app import usuarios
usuarios = list()

def menu():
    """
    Printa menu de opções no terminal
    """
    print()
    print('1 - Cadastrar novos usuarios')
    print('2 - Listar usuarios')
    print('3 - Atulizar usuarios')
    print('4 - Deletar usuarios')
    print('5 - Encerrar')

def cadastrar_usuario(nome, cpf):
    usuario = {
        'nome' : nome,
        'cpf' : cpf
    }
    usuarios.append(usuario)

    return f'Usuario {usuario['nome']} cadastrado com sucesso!'