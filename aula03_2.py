#_*_ coding:utf-8 _*_
nome=input("Digite o nome do aluno: ")#essa variavel recebe o nome de um aluno

#As variáveis a seguir, recebem as notas de um aluno
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))


#A variável "media" a seguir calcula a média dos alunos
media = (nota1+nota2+nota3+nota4)/4

#ENSINEI A CONDIÇÃO IF E ELSE NA AULA ANTERIOR, CASO ESTEJA PERDIDO(A), VOLTE LÁ SE ENCONTRA NESSE REPOSITÓRIO, COM O NOME: aula03.py 
if(media>7.00):
    print(f"{nome} foi Aprovado! com a média de {media}")

#ESSA É A CONDIÇÃO "NOVA" , ELA SÓ É EXECUTADA CASO O IF SEJA FALSA, MAS PERCEBA, ELA TAMBÉM RECEBE UMA CONDIÇÃO, E TEM FUNCIONALIDADE IDÊNTICA AO DO IF.
elif(media<7.00 and media>4.00):
    print(f"{nome} foi reprovado! com a média de {media} e pode fazer uma recuperação!")

#COMO EXPLICADO NA PRIMEIRA PARTE DESSA AULA, NO CASO DESSA TAMBÉM, O ELSE SÓ É EXECUTADO CASO TODAS AS CONDIÇÕES IF's E ELIF's SEJAM FALSAS
else:
    print(f"{nome} foi reprovado com a média de {media} e não poderá fazer recuperação!")

#DETALHE IMPORTANTE !!!!
#PODEMOS USAR VÁRIOS IF's  NO MESMO CÓDIGO, ASSIM COMO ELIF's E ELSE's, MAS TUDO DEPENDE DA LÓGICA DAQUILO QUE VOCÊ ESTÁ PROGRAMANDO.