""" 
Problema: João precisa calcular seu Índice de Massa Corporal (IMC) para avaliar seu peso ideal. 
Sabendo que a fórmula para calcular o IMC é: peso ÷ altura², 
crie um programa que calcule e informe a classificação do IMC.
"""
print("IMC de João")


def calcular_imc(peso, altura):
    imc = peso / pow(altura ,2)#Calculo do imc potencia pow
    if imc > 40:
        return('Você está com Obesidade Mórbida Classe III', imc)
    elif imc >= 35 and imc < 39.9:
        return ('Você está em Obesidade Classe II.', imc)
    elif imc >= 30 and imc < 34.9:
        return ("Você está em Obesidade Classe I .", imc)
    elif imc >= 25 and imc < 29.9:
        return ("Você está Excesso de Pesso .", imc)
    elif imc >= 18.5 and imc < 24.9:
        return ("Você está Peso Ideal .", imc)
    else:
        return ("Você esta Muito abaixo do peso.", imc)

peso=float(input("Peso Resolução proposta: "))
altura=float(input("Altura Resolução proposta:"))
imc_valor=calcular_imc(peso, altura )#Chamada da função   
print(imc_valor)
#Exemplo Aula
    
def calculadoraImc(peso, altura):
     imc = peso/(altura*altura) * 10000
     if (imc <= 18.5): return "Magreza",imc
     elif (imc > 18.5) and (imc <= 24.9): return "Saudavel",imc
     elif (imc >= 25) and (imc <= 29.9): return "Sobrepeso",imc
     elif (imc > 30) and (imc <= 34.9): return "Obesidade grau 1",imc
     elif (imc > 35) and (imc <= 39.9): return "Obesidade severa grau 2",imc
     else : return "Obesidade morbida grau 3",imc

peso=float(input("Peso Exemplo aula: "))
altura=float(input("Altura Exemplo aula:"))
resultado = calculadoraImc(peso,altura)
print(resultado)
    
    
    


