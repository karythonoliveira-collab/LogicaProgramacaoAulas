'''
    Programa: Sorteio V.1.0
    Importando bibliotecas
    Aula 04: 19/08/2025

    Random: escolha aleatoria
    Descrição: sistema recebe o nome dos candidatos e realiza o sorteio
'''
# importando bibliotecas (lib)
import random

nome1 = input("Digite o primeiro nome: ")
nome2 = input("Digite o segundo nome: ")
nome3 = input("Digite o terceiro nome: ")
nome4 = input("Digite o quarto nome: ")
nome5 = input("Digite o quinto nome: ")

lista_nomes = [nome1, nome2, nome3, nome4, nome5]

escolhido = random.choice(lista_nomes)
print(escolhido)
