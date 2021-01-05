lista = []
par = []
impar = []
while True:
    n = int(input('Digite um número: '))
    r = str(input('Quer continuar? S/N ')).upper()[0]
    lista.append(n)
    if r in 'N':
        if n %2 == 0:
            par.append(n)
            break
        if n %2 != 0:
            impar.append(n)
        break
    elif n %2 == 0:
        par.append(n)
    else:
        impar.append(n)
lista.sort()
par.sort()
impar.sort()
print(f'Números Pares {par}')
print(f'Números Ímpares {impar}')
