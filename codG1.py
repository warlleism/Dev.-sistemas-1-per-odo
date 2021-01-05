cadas = {}
cadas1 = []
while True:
    cadas.clear()
    cadas['nome'] = str(input('Digite seu nome: '))
    while True:
        cadas['sexo'] = str(input('Digite seu sexo: [M/F] ')).upper()[0]
        if cadas['sexo'] in 'MF':
            break
        else:
           print('Erro. Digite apenas M ou F')
    cadas['idade'] = int(input('Digite sua idade: '))
    cadas1.append(cadas.copy())
    while True: 
        res = str(input('Quer continuar: [S/N] ')).upper()[0]
        if res in 'SN':
            break
        else:
           print('Erro. Digite apenas S ou M')
    if res == 'N':
        break
print(cadas1)
       
        
        
