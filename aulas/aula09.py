#TUPLAS 

#Esse import é correspondente a padronização dos campos , explicado no fim desse arquivo.
from collections import namedtuple


#É assim que criamos uma tupla:
tupla = ("Dennis" , 19, "MA") 
''' 
#Também posso criar assim:
tupla = "Dennis" , 19, "MA" ,

#sem parenteses, a vírgula no final é opcional:
'''


#A palavra reservada "in" permite caçar um determinado elemento na tupla , e retorna se tem ou não 
print("Dennis" in tupla)

#Com o index , é possível encontrar o índice de um determinado dado na tupla
print(tupla.index(19))

#O count retorna a quantidade de um elemento na tupla(quantas vezes ele se repete)
print(tupla.count("Dennis"))

#Dando nome aos campos  da tupla, explico melhor no vídeo , link: https://www.youtube.com/watch?v=BVn3eRgySVc
Cliente =  namedtuple("Cliente" , ["nome", "idade", "Estado"])

#Padronizo a tupla com o nome dos campos que acabei de declarar
tupla = Cliente("Dennis" , 19 , "MA")


#Por fim, imprimo a tupla padronizada
print(tupla)