# revisao
'''
nome = "Gomes"
idade = 16

print(type(nome)) # ver o tipo de dados da variavel

idade = float(idade)# conversao padrao

print(f'O meu nome é {nome} {type(nome)} tenho {idade} anos de idade {idade + 1}', nome,idade)

nome_usuario = input("Digite seu nome: ") # padrao: string

peso = float(input("Digite seu peso").replace(',','.').lower())

if peso >= 50: # verifica se e verdade
    print('Acima de 50 kilos')
else: # se nao for verdadeiro
    print('Abaixo de 50 kilos')

if peso >=50:
    print('Acima de 50 kilos.')
elif peso >=80:
    print('Acima de 80 kilos.')
elif peso >=90:
    print('Acima de 90 kilos.')
else:
    print("abaixo do peso")


'''
'''
    Problema: crie um sistema que calcule o indice de massa corporal(IMC)
    do usuario, mostre o valor do IMC na tela, e retorne se o usuario esta
    no peso ideai ou se precisa emagrecer ou engordar mais. Ultilize a tabela
    do IMC para definir os valores.

    imc = peso / (altura * altura) 

    18,5 ou menos
Abaixo do normal

Entre 18,5 e 24,9
Normal

Entre 25,0 e 29,9
Sobrepeso

Entre 30,0 e 34,9
Obesidade grau I

Entre 35,0 e 39,9
Obesidade grau II

Acima de 40,0
Obesidade grau III


print(40*"-",'CALCULADORA DE IMC',40*'-')
altura = float(input('Digite o seu altura: ').replace(',','.'))
peso = float(input('Digite o seu peso: ').replace(',','.'))

imc = peso / (altura * altura)

print()
print(f'Seu IMC é: {imc:.2f}')

if imc <= 18.5:
    print('Abaixo do normal')
elif imc <= 24.9:
    print('Normal')
elif imc <= 29.9:
    print('Sobrepeso')
elif imc <= 34.9:
    print('Obesidade grau I')
elif imc <= 39.9:
    print('Obesidade grau II')
else:
    print('Obesidade grau III')



    Problema 2: Um elevador de carga possui capacidade para 200kg. Crie
    um programa que receba do usuario seu peso e o peso da carga e veri-
    fica se a carga está autorizada a usar o elevador ou não.


# TODO:

limite = 200

peso_usuario = float(input('Digite seu peso: ').replace(',','.'))
peso_carga = float(input('Digite o peso da carga: ').replace(',','.'))

if (peso_usuario + peso_carga ) >= limite:
    print('Não autorizado.')
else:
    print('Autorizado')


print(40*"-",'CALCULADORA DE IMC',40*'-')

while True:

    altura = float(input('Digite o seu altura: ').replace(',','.'))
    peso = float(input('Digite o seu peso: ').replace(',','.'))

    imc = peso / (altura * altura)

    print()
    print(f'Seu IMC é: {imc:.2f}')

    if imc <= 18.5:
        print('Abaixo do normal')
    elif imc <= 24.9:
        print('Normal')
    elif imc <= 29.9:
        print('Sobrepeso')
    elif imc <= 34.9:
        print('Obesidade grau I')
    elif imc <= 39.9:
        print('Obesidade grau II')
    else:
        print('Obesidade grau III')

    opcao = input('Deseja calcular novamente? S - Sim | N - Não: ').lower()

    if opcao == 's':
        continue
    elif opcao == 'n':
        print('Saindo do sistema!')
        break
    else:
        print('Opção inválida')

print(40*"-",'CADASTRO DE USUÁRIO',40*'-')
nome = input('Digite seu nome: ').upper()
cpf = input('Digite seu CPF: ')
telefone = input('Digite seu Telefone: ')
dt_nascimento = int(input('Digite seu ano de nascimento: '))
print(80*"=")
while True:
    # menu principal
    print(40*"-",'Sistema Console 2° DS',40*'-')
    print('1 - Calculadora IMC')
    print('2 - Maioridade')
    print('3 - Calculadora')
    print('4 - Dados pessoais')
    print('5 - Feliz natal')
    print('6 - Sair')
    opcao = input('Digite uma opção: ')
    if opcao == "1":
        altura = float(input('Digite o seu altura: ').replace(',','.'))
        peso = float(input('Digite o seu peso: ').replace(',','.'))
        imc = peso / (altura * altura)
        print()
        print(f'Seu IMC é: {imc:.2f}')

        if imc <= 18.5:
            print('Abaixo do normal')
        elif imc <= 24.9:
            print('Normal')
        elif imc <= 29.9:
            print('Sobrepeso')
        elif imc <= 34.9:
            print('Obesidade grau I')
        elif imc <= 39.9:
            print('Obesidade grau II')
        else:
            print('Obesidade grau III')

    elif opcao == "2":
        ano_atual = 2025
        idade = ano_atual - dt_nascimento
        print(nome, 'é maior de idade.' if idade >= 18 else 'é menor de idade.')
    elif opcao == "3":
        print(30*'-',"Calculadora")
        while True:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            print()
            print("1 - Soma")
            print("2 - Divisão")
            print("3 - Subtração")
            print("4 - Multiplicação")
            print("5 - Sair")

            opcao_calculo = input('Escolha uma operação matemática: ')

            if opcao_calculo == "1":
                print(f'Resultado da Soma é: {num1 + num2}')
            elif opcao_calculo == "2":
                print(f'Resultado da Divisão é: {num1/num2}')
            elif opcao_calculo == "3":
                print(f'Resultado da Subtração é: {num1 - num2}')
            elif opcao_calculo == "4":
                print(f'Resultado da Multiplicação é: {num1*num2}')
            elif opcao_calculo == "5":
                break
            else:
                print('Opção Inválida')
            
    elif opcao == "4":
        print(50*'_')
        print(f'| Nome: {nome} | Telefone:          {telefone}      |')
        print(f'| CPF:  {cpf}  | Data de Nascimento {dt_nascimento} |')
        print(50*'-')
    elif opcao == "5":
        linhas = 15
        j = 1
        while j<= linhas:
            espacos = linhas - j
            estrelas = 2 * j - 1

            print(" " * espacos + "^" * estrelas)
            j +=1
        
    elif opcao == "6":
        print("Saindo do sistema!")
        break
    else:
        print("Opção inválida!")
'''


nome = "Gomes"

for i in nome:
    print(i.replace(i,'*'))