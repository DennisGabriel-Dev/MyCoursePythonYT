name=input("Digite o nome do aluno: ")
nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))
nota4 = float(input("Digite a nota 4: "))

media = (nota1+nota2+nota3+nota4)/4

if(media>7.00):
    print(f"{name} foi Aprovado! com a média de {media}")

elif(media<7.00 and media>4.00):
    print(f"{name} foi reprovado! com a média de {media} e pode fazer uma recuperação!")

else:
    print(f"{name} foi reprovado com a média de {media} e não poderá fazer recuperação!")