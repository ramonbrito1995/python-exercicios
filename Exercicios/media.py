#Faça um programa que contenha uma função que calcule a média de cinco alunos (as notas de
#cada aluno deverão ser distintas);

def media(nota_1,nota_2,nota_3):
    media = (nota_1+nota_2+nota_3)/3
    print("%.2f"%media)

print("Aluno 1:")
media(8,5,6)
print("")

print("\nAluno 2:")
media(1,7,6)
print("")

print("\nAluno 3:")
media(5,5,9)
print("")

print("\nAluno 4:")
media(0,5,7)
print("")

print("\nAluno 5:")
media(10,5,6)
print("")


