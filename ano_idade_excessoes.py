"""Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

Caso o usuário não digite um número ou apareça um inválido no campo do ano, o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

"""
contador = 0
ano_nascimento = False

nome = input("Digte seu Nome: ")
ano_atual = 2023


while ano_nascimento == False:
    
    try:
        ano_nascimento = int(input("Digite ano Nascimento: "))
        
        if ano_nascimento >= 1922 and ano_nascimento <= 2021:
            ano_nascimento == True
        else:
            ano_nascimento = int(input("Digite Novamente ano Nascimento: "))      
    except:
            print("Caracter inválido, por favor digite ano Nascimento")  
            
idade = (ano_atual - ano_nascimento)
print('Nome:', nome, 'Idade', idade,'Anos')
