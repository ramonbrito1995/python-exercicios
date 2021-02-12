"""Faça uma função que calcule se o resultado do exame do paciente está "bom", "médio" ou
"ruim". O algoritmo deve conter, pelo menos, três pacientes (um em cada situação)."""


def exame(resultado):
    if resultado > 7 and resultado <=10:
        print("\nBom!"
              "\nContinuar assim!")
    elif resultado> 4 and resultado<6:
        print("\nMédio!"
              "\nBuscar se cuidar mais e fazer acompanhamento médico!")
    else:
        print("\nRuim!\nProcurar equipe médica!")

print("\n")
print("="*50)
print("Paciente 1:".center(45))
print("="*50)
paciente_1 = float(input("\nFavor dizer o resultado do exame.(Escala de 0 a 10):  "))
exame(paciente_1)

print("\n")
print("="*50)
print("Paciente 2:".center(45))
print("="*50)
paciente_2 = float(input("\nFavor dizer o resultado do exame.(Escala de 0 a 10):  "))
exame(paciente_2)

print("\n")
print("="*50)
print("Paciente 3:".center(45))
print("="*50)
paciente_3 = float(input("\nFavor dizer o resultado do exame.(Escala de 0 a 10):  "))
exame(paciente_3)




