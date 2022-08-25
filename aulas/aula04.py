#_*_ coding:utf-8 _*_
#Nessa aula trataremos dos métodos em string.
s = " Hello Friend! "

#O método upper serve para deixar todas as letras maíusculas de uma variável do tipo string.
print(s.upper())

print("------------------------")

#O método lower é o inverso do upper, ele serve para deixar todas as letras minúsculas de uma variável do tipo string. 
print(s.lower())

print("------------------------")

#O método index serve para encontrar a posição de uma determinada letra em  uma frase dado a sua variável do tipo string. 
print(s.index("o"))

print("------------------------")

#O método replace substitui uma letra ou campo de letras por outra(s),
#basta informar a(s) letra(s) que serão substituídas no primeiro parâmetro, e em seguida a(s) letra(s) que a(s) substituirá(ão).
print(s.replace("e","x"))

print("------------------------")

#O método strip serve para retirar os espaços das extremidades(início e fim) de uma determinada variável do tipo string.
print(s.strip())

print("------------------------")

#O método split serve para "dividir" à variável em arrays. 
print(s.split())
