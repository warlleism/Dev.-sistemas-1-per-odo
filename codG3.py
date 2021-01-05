print('''Quais dos três diferentes novos “mix” de sabores você Mais gostou? 
[1] Para Mix "1" 
[2] Para Mix "2" 
[3] Pra Mix "3" ''')
mix1 = 0
mix2 = 0
mix3 = 0
while True:
    mix = str(input('Escolha o Mix que mais gostou: '))
    if mix in "0":
        break
    elif mix in '1':
        mix1 = mix1 + 1
    elif mix in '2':
        mix2 = mix2 + 1
    elif mix in '3':
        mix3 = mix3 + 1
print(f'Mix 1 recebeu {mix1} votos! {mix1/(mix1 + mix2 + mix3)* 100:.0f}%')
print(f'Mix 2 recebeu {mix2} votos! {mix2/(mix2 + mix3 + mix1)* 100:.0f}%')
print(f'Mix 3 recebeu {mix3} votos! {mix3/(mix3 + mix1 + mix2)* 100:.0f}%')


