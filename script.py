from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print('BORA JOGAR JOKENPO?')

print('''SUAS OPÇÕES
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura
''')
jogador = int(input('Qual é a sua jogada? '))

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')
sleep(1)

print('=' * 25)
print(f'Computador jogou {itens[computador]} ')
print(f'Jogador jogou {itens[jogador]} ')
print('=' * 25)

if computador == 0: #pc jogou pedra
    if jogador == 0:
        print('EMPATE') #jogador jogou pedra

    elif jogador == 1:
        print('JOGADOR VENCE') #jogador jogou papel

    elif jogador == 2:
        print('COMPUTADOR VENCE') #jogador jogou tesoura

    else:
        print('JOGADA INVÁLIDA')

elif computador == 1: #pc jogou papel
    if jogador == 0:
        print('[COMPUTADOR VENCEU') #jogador jogou pedra

    elif jogador == 1:
        print('EMPATE') #jogador jogou papel

    elif jogador == 2:
        print('JOGADOR VENCEU') #jogador jogou tesoura

    else:
        print('JOGADA INVÁLIDA')

elif computador == 2: #pc jogou tesoura
    if jogador == 0:
        print('JOGADOR VENCEU') #jogador jogou pedra

    elif jogador == 1:
        print('COMPUTADOR VENCE') #jogador jogou papel

    elif jogador == 2:
        print('EMPATE') #jogador jogou tesoura

    else:
        print('JOGADA INVÁLIDA')