'''Exercício Python 084: Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:'''
#A) Quantas pessoas foram cadastradas.
#B) Uma listagem com as pessoas mais pesadas.
#C) Uma listagem com as pessoas mais leves.


pessoas = list()
dados = list()
peso_maior = peso_menor = 0
cont = 0
while True:
    dados.append(str(input("Nome: ")))
    dados.append(float(input("Peso: ")))
    if len(pessoas)==0:
        peso_maior = peso_menor = dados[1]
    else:
      if dados[1] > peso_maior:
        peso_maior = dados[1]
      if dados[1] < peso_menor:
        peso_menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    cont += 1
    resposta = input("Quer continuar? (Sim ou não?")
    if resposta.lower() in 'não':
        break

cont = len(pessoas)

x = 0
y = 1

for p in range(0, cont):
    print(pessoas[x])
    x+= 1
           
for p in pessoas:
    if p[1] == peso_maior:
        print("\nO maior peso é do:",p[0])
print(peso_maior)

for p in pessoas:
    if p[1] == peso_menor:
        print("O menor peso é do:",p[0])
print(peso_menor)


