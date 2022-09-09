# Criamos a Lista
motos = ['biz', 'xj6' ,'titan']


# o metodo .append adiciona um item no fim da lista
motos.append('fan')
print(motos)

# no .insert informamos a posicao da lista que queremos colocar tal item e a informacao do item logo em seguida
motos.insert(-1, 'pop')

# o .pop remove o item mas é possível guardar dentro de uma variavel,  a posicao entre os "()" não eh obrigatoria, pois se eu nao informar , ele simplesmente remove o ultimo elemento da lista   
comprado = motos.pop(1)

# o .del deleta de vez um item da lista, deixando-o inutilizavel
del motos[-1]

# diferente do pop, no .remove colocamos o nome do item e não a posição , o .remove apaga de vez o item da lista deixando-o inutilizavel
motos.remove('titan')

'''
#imprimimos a lista
print(motos)
'''