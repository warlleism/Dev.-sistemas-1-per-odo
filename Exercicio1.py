temporario = []
principal = []
maior = 0
menor = 0
while True:
    temporario.clear()
    temporario.append(str(input('Digite seu nome: ')))
    temporario.append(float(input('Informe seu peso: ')))
    if len(principal) == 0:
        maior = temporario[1]
        menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
             menor = temporario[1]
    principal.append(temporario[:])
    nex = str(input('Deseja continuar? [S/N]')).upper()[0]
    if nex in 'Nn':
        break
print(f'Os dados foram {principal}')
print(f'Quantidade de pessoas cadastradas {len(principal)}')
for p in principal:
    if p[1] == maior:
        print(f'{p[0]} tem o maior peso = {maior}Kg')
for p in principal:
    if p[1] == menor:
        print(f'{p[0]} tem o menor peso = {menor}Kg')
 
