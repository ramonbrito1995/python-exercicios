"""Faça um programa que calcule a diferença entre a sua idade e a da mulher de STEM que você
pesquisou na última aula. Você também deve comparar o estado e país de vocês, e exibir isso
na tela de uma maneira que fique claro para quem está lendo."""



def idade(sofia):
    comp_idade = 1995 - sofia
    print(f'A diferença de idade entre Sofia e Ramon é: {comp_idade} anos.'.center(50))

def pais():
    print("Sofia nasceu na Rússia em Moscou e Ramon no Brasil no RJ.".center(50))
    print("Sofia morreu em 1891.".center(50))

print("")
print("="*150)
idade(1850)
pais()