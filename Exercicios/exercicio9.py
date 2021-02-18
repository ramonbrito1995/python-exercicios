'''Exercício Python 085: Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.'''

valores = [ [], [] ]
dados = 0
x = 0
for c in range(0,7):
     dados = int(input("Digite um valor : "))
     if dados%2==0:
          valores[0].append(dados)
     else:
         valores[1].append(dados)


print(valores)
print(len(valores[0]))
print(len(valores[1]))