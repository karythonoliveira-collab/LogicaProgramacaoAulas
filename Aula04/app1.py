'''
    Programa: Contagem regressiva
    Importando bibliotecas
    Aula 04: 19/08/2025
'''

# importando bibliotecas (lib)
import os
from time import sleep

cont = input('Digite um numero inteiro: ')

try:
    cont_int = int(cont)
    while cont_int >= 0:
        os.system('cls')
        print(f'Contagem regressiva: {cont_int}...')
        sleep(1)
        cont_int -= 1
        os.system('cls')
except:
    print('Digite um numero válido!')

print('Fim da contagem!')