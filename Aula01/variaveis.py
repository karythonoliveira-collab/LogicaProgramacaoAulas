# comentario de linha
'''
print("Olá mundo, esse é o meu \nprimeiro script em \npython")
print(30*"-","Concatenando texto",30*"-")
# comentario de linha
print('Essa é a segunda linha do meu codigo')


comentario de bloco
comentario de bloco


nome = "karython Gomes"
idade = 27
ano_nascimento = 1998
print("Olá, me chamo", nome,"tenho", idade,"anos de idade e " \
"sou de", ano_nascimento)

# Tipos de variaveis

nome = "gomes"
idade = 25
altura = 1.75
ativo = True

print("O tipo da varivavel nome é:",type(nome))
print("O tipo da varivavel idade é:",type(idade))
print("O tipo da varivavel altura é:",type(altura))
print("O tipo da varivavel ativo é:",type(ativo))
print()
# operadores
print(30*'-','operadores aritmeticos',30*'-')
num1 = 8
num2 = 2

soma = num1 + num2
divi = num1 / num2 # divisao comum
divisao_inteira = num1 // num2 # divisao inteira
mult = num1 * num2
expo = num1 ** num2
sub  =  num1 - num2
resto = num1 %2


print('Resultado da soma',num1, "+", num2, "é:", soma)
print('Resultado da divisão',num1, "/", num2, "é:", divi)
print("Resultado da divisao inteira é:",divisao_inteira)
print('Resultado da multiplicação',num1, "X", num2, "é:", mult)
print('Resultado do expoente é:', expo)
print('Resultado da subtração',num1, "-", num2, "é:", sub)
print('Resultado do resto de', num1, 'é:',resto)

print()
print(30*'-','operadores de comparação',30*'-')
# operadores de coparação
num1 > num2
num1 < num2
num1 == num2
num1 >= num2
num1 <= num2
num1 != num2

ano = 2025
print("ano atual",ano)
ano += 1
print('ano acrecido de +1',ano)
ano -= 1
print('Ano decrecido de -1',ano)

# operadores logicos
# AND, OR, NOT

print()
print(30*'-','Entrada de dados',30*'-')

nome_usuario = input("Digite o seu nome: ")
print('Seja bem-vindo ao sistema python', nome_usuario)

print()
print(30*'-','Calculadora',30*'-')

numero1 = float(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))


# tipos de dados
# float = numeros reais, ou seja, tem ',', exemplo: 5.20
# int   = numeros inteiros
# str   = texto, conjunto de caracteres
# bool  = valores logicos como True e False

soma = numero1 + numero2
divi = numero1 / numero2
mult = numero1 * numero2
sub  =  numero1 - numero2

print('Resultado da soma',numero1, "+", numero2, "é:", soma)
print('Resultado da divisão',numero1, "/", numero2, "é:", divi)
print('Resultado da multiplicação',numero1, "X", numero2, "é:", mult)
print('Resultado da subtração',numero1, "-", numero2, "é:", sub)
'''
print()
print(30*'-','Convertendo tipos de dados',30*'-')
'''
ano_nascimento = input("Digite seu ano de nascimento: ")
print(type(ano_nascimento))
# convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))


n1 = 10
n2 = 20

print("A soma é:", n1+n2, type(n1), float(n2))
'''
saudacao = input('Digite seu nome: ')
cpf = input('Digite seu CPF: ')
telefone = input("Digite seu telefone: ")

print(20*'-','Dados Pessoais',20*'-')
print('Nome:', saudacao)
print('CPF:', cpf, '| Telefone:',telefone)
print(50*'-')
