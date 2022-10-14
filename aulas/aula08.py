motos = [ 'xj6' , 'biz' ,'titan' , 'pop']

#O método sort ordena a lista em ordem alfabetica
motos.sort()

#Se colocarmos o reverse=True dentro dos parenteses , a lista é ordenada da última letra para a primeira...
motos.sort(reverse=True)

#O método sorted ordena a lista temporariamente, ao contrário do sort
print(sorted(motos))

#len é útil para ler o tamanho de uma lista
print(len(motos))

#O método upper deixa TODAS as letras de uma determinada palavra ou frase em maiúsculas.
print(motos[1].upper())

#O método lower deixa  TODAS as letras de uma determinada palavra ou frase em minúsculas.
print(motos[1].lower())

#O método capitalize deixa apenas a primeira letra em maiúscula.
print(motos[1].capitalize())

#O método title faz o mesmo que o capitalize.
print(motos[1].title())

print(motos)