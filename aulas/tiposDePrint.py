#Tipos de prints em Python !!!

name = input("Digite seu nome: ")

#formato de print mais usado por iniciantes, pois é agradável quando não se tem muitos dados para serem manipulados.
print("Boa Noite", name)

#cuidado com esse formato de print, pois ele só permite "juntar"/"somar" dados do mesmo tipo, diferente do print mostrado acima.
print("Boa Noite " + name)

#aqui temos um f antes do que será mostrado na tela, esse f serve para dizer que teremos uma "FORMATAÇÃO" nos dados que vierem dentro das chaves: {}.
print(f"Boa Noite {name}")

#abaixo temos um método parecido com o anterior , a lógica é quase a mesma do anterior, no entanto informamos os dados 
#que serão recebidos dentro do format assim: format(dado1,dado2) que irão depender da quantidade de dados a serem recebidos.
print("Boa Noite {}" .format(name))

#Lembrando que ambos imprimarão na tela a mesma coisa, mas quando se trata de problemas mais complexos, nem sempre o mais simpes será a melhor opção.

#Eu sinceramente prefiro o terceiro método quando vou trabalhar com vários dados :).