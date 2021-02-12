"""Crie um algoritmo que multiplique dois valores aleatórios entre 1 e 50. Você deverá usar
condicionais e funções nesse processo."""

def multiplicacao(valor_1,valor_2):
    multiplica = valor_1*valor_2
    print(f"\nA multiplicação dos dois valores é: {multiplica}!""\n")
    
valor1 = int(input("Digite um valor de 1 a 50? "))
valor2 = int(input("Digite um valor de 1 a 50? "))

if 0< valor1 < 51 and  0 < valor2 < 51:
    multiplicacao(valor1,valor2)
else:
    print("Você precisa digitar valores entre 1 e 50!")
    valor1 = int(input("Digite um valor de 1 a 50? "))
    valor2 = int(input("Digite um valor de 1 a 50? "))
    multiplicacao(valor1,valor2)
