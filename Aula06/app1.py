# dicionario

usuario = {
    'nome':'Gomes',
    'idade': 26
}


print(type(usuario))
print(usuario)

#print(f'Nome: {usuario['nome']}')
#print(f'Idade: {usuario["idade"]}')

usuarios = ['gomes', 'nunes', 'cris', 'andre']
print(usuarios)
print(f'Nome: {usuarios[-2]}')

print(f'Nome: {usuario.get('nome')}')