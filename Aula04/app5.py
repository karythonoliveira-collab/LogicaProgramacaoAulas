'''
    Programa: Adivinhação V.1.0
    Importando bibliotecas
    Aula 04: 19/08/2025

    Random: escolha aleatoria
    Descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''

# importando lib
from random import randint

print('Tente adivinhar o numero!')
num1 = int(input("Digite um numero: "))

num_secreto = randint(1,2)

if num1 == num_secreto:
    print('Parabéns, voce ganhou!')
else:
    print('Voce perdeu')
    print(f'O numero correto é {num_secreto}')