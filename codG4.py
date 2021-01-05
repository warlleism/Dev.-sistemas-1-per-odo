cadaSenha = []
cadaUsua = []
while True:
    nome = str(input('Nome do usuário: '))
    senha = input('Senha: ')
    completo = str(input('Deseja continuar? S/N ')).upper()
    if completo in 'S':
        if senha == nome:
            print('Senha inválida! Não pode ser igual ao nome.')
            senha = input('Escolha uma nova senha: ')
        elif senha != nome:
            cadaSenha.append(senha)
            cadaUsua.append(nome)
            print('Usuário e Senha aceitas!')
    else:
        break
print(cadaUsua)
print(cadaSenha)

