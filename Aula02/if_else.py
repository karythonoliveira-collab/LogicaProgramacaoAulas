# concatenação
# quebra de linha
# formatando decimais
# alterando virgula e ponto
# if else
# operador ternario

#FIXME - concatenação com +
'''
nome = "Gomes"
idade = 26
altura = 1.75

# saida de dados
print('Olá, meu nome é, ' + nome + ', tenho ' + str(idade) + ' anos de idade')

#FIXME - concatenação com ,
print('Olá, meu nome é,', nome,',tenho', idade, 'anos de idade')

#FIXME - concatenação com format
print('Olá, meu nome é, {} , tenho  {}  anos de idade'.format(nome,idade))

#FIXME - concatenação com f-string
print(f'Olá, meu nome é {type(nome)} e tenho {idade+1} anos de idade')


# eliminando quebra de linha
print('O Sábio sabia ', end='')
print('que sabiá sabia assobiar.')


valor = 1.23456789

# exibindo o valor com duas casas depois da virgula
print(f'{valor:.2f}')

print(50*'=')
peso = input('Digite seu peso: ').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}'.replace('.',','))

'''
'''
nome = input('Digite seu nome:')
idade = int(input('Digite sua idade: '))

print('Antes do if')
if idade >= 18:
    print('Você é maior de idade!')
    print('Você esta dentro do bloco IF')
else:
    print('Você é menor de idade!')
    print('Você está dentro do bloco ELSE')
print('Você está fora da estrutura condicional if else')
'''

num1 = 10

if num1 %2 ==0:
    print('Numero par')
else:
    print('Numero impar')

print(40*'-','BOLETIM ESCOLAR',40*'-')  # upper - caixa alta; lower - caixa baixa
nome_aluno = input('Digite o nome do aluno: ').upper()
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
nota4 = float(input('Digite a quarta nota: '))
print()

media = (nota1 + nota2 + nota3 + nota4)/4

# >= 7: aprovado
# >= 5: recuperacao
# reprovado

if media >=7:
    print(f'{nome_aluno}!!!Aluno Aprovado!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')

elif media >= 5:
    print(f'{nome_aluno}!!!Aluno de Recuperação!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')
else:
    print(f'{nome_aluno}!!!Aluno Reprovado!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')