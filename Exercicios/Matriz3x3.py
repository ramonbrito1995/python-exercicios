'''Exercício Python 086: Crie um programa que declare uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

Exercício Python 087: Aprimore o desafio anterior, mostrando no final: 
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha
'''

matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = 0
soma1 = 0
maior_valor = 0

#criando uma matriz 3x3
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input("Digite um número: "))
        if matriz[l][c]%2 == 0:   #somando todos os números pares da matriz
            soma += matriz[l][c]
print("-="*30)
print("Matriz 3x3: ")
for l in range(0,3):
    for c in range(0,3):
        print(f"[{matriz[l][c]:^5}]", end = "")
    print()

print("-="*30)
#Pegando o maior valor da 2° linha
for c in range(0,3):
   if matriz[1][c] > maior_valor:
       maior_valor = matriz[1][c]

#somando os valores da 3 coluna
soma1 = sum([ x[2] for x in matriz])


print(f"\nMaior valor da 2° linha é :{maior_valor}.")
print(f"A soma de todos os números pares é :{soma}")
print(f"A soma dos elementos da 3 coluna é {soma1}.")


