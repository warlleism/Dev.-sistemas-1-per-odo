listaaltM = []
listaaltF = []
contM = 0
contF = 0
somaM = 0
somaF = 0
while True:
    sexo = str(input('Qual seu sexo? M/F ')).upper()[0]
    altura = float(input('Qual sua altura? '))
    if sexo in 'Mm':
        listaaltM.append(altura)
        somaM += altura
        contM += 1
        mediaM = somaM/contM
        continuar = str(input('Deseja continuar? S/N'))
    elif sexo in 'Ff':
        listaaltF.append(altura)
        somaF += altura
        contF += 1
        mediaF = somaF/contF
        continuar = str(input('Deseja continuar? S/N'))
    if continuar in 'Nn':
        break
print(f'O Maior Homem tem {max(listaaltM)} Metros de altura')
print(f'A Maior Mulher tem {max(listaaltF)} Metros de altura')
print(f'A média da altura dos homens é {mediaM}')
print(f'A média da altura das mulheres é {mediaF}')

